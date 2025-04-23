import pygame

from entities.player.Player import Player
from log.LogSubject import LogSubject
from items.equipables.EquipableItem import EquipableItem
from items.usables.UsableItem import UsableItem

from gameMap.MapSettings import *
from UI.Colors import *

class ItemManager:

    def __init__(self):
        self.equipable_items = []
        self.usable_items = []

    def all_items(self):
        return self.equipable_items + self.usable_items

    def create_item(self, item):
        if isinstance(item, EquipableItem):
            self.equipable_items.append(item)
        elif isinstance(item, UsableItem):
            self.usable_items.append(item)

    def erase_item(self, item):
        if isinstance(item, EquipableItem):
            if item in self.equipable_items:
                self.equipable_items.remove(item)
        elif isinstance(item, UsableItem):
            if item in self.usable_items:
                self.usable_items.remove(item)

    def check_for_pickups(self, player: Player, inventory):
        """ Checks if the player is on the same tile as an item and adds it to the inventory. """
        log_subject = LogSubject()

        for item in self.usable_items[:]:
            if player.get_position() == item.get_position():
                inventory.add_item(item)
                log_subject.notify_log_observer(f"Picked up a {item.item_name()}.")
                self.erase_item(item)
        
    def item_visibility(self, player):
        for item in self.all_items():
            distance_to_item = item.get_position().distance(player.get_position())
            if distance_to_item <= player.visibility_radius:
                item.set_visible(True)
                if not item.is_discovered():
                    item.set_discovered(True)
            else:
                item.set_visible(False)

    def draw_item(self, display_surface):
        for item in self.all_items():
            if isinstance(item, EquipableItem):
                x_pos = item.get_position().x * tile_size
                y_pos = item.get_position().y * tile_size + 9
            elif isinstance(item, UsableItem):
                x_pos = item.get_position().x * tile_size + 9
                y_pos = item.get_position().y * tile_size

            item_rect = (x_pos, y_pos, item_size, item_size)

            if not item.is_discovered():
                pygame.draw.rect(display_surface, undiscovered_area_color, item_rect)
            elif item.is_visible():
                pygame.draw.rect(display_surface, item.visible_color, item_rect)
            else:
                pygame.draw.rect(display_surface, item.invisible_color, item_rect)

            pygame.draw.rect(display_surface, (0, 0, 0), item_rect, 1)
