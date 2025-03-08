import pygame

from entities.Player import Player
from items.equipables.EquipableItem import EquipableItem
from items.usables.UsableItem import UsableItem

from gameMap.MapSettings import *
from UI.Colors import *

class ItemManager:

    def __init__(self):
        self.equipable_items = []
        self.usable_items = []

    def add_item(self, item: EquipableItem):
        self.equipable_items.append(item)
    
    def add_item(self, item: UsableItem):
        self.usable_items.append(item)

    def all_items(self):
        items = self.equipable_items + self.usable_items
        return items

    def item_visibility(self, player: Player):
        for item in self.all_items():
            distance_to_item = item.get_position().distance(player.get_position())
            if distance_to_item <= player.visibility_radius:
                item.set_visible(True)
                if not item.is_discorvered():
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

            if not item.is_discorvered():
                pygame.draw.rect(display_surface, undiscovered_area_color, item_rect)
            elif item.is_visible():
                pygame.draw.rect(display_surface, item.visible_color, item_rect)
            else:
                pygame.draw.rect(display_surface, item.invisible_color, item_rect)

            pygame.draw.rect(display_surface, (0, 0, 0), item_rect, 1)
