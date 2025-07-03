import pygame
from sys import exit

from entities.player.Player import Player
from entities.player.Inventory import Inventory
from gameMap.tiles.TileManager import TileManager
from items.ItemManager import ItemManager
# from items.usables.HealthPotion import HealthPotion
# from items.usables.ManaPotion import ManaPotion
from panels.MainMenu import MainMenu
from panels.CharacterCreationPanel import CharacterCreationPanel
from log.LogSubject import LogSubject
from panels.LogPanel import LogPanel

from panels.PanelSettings import *
from gameMap.MapSettings import *
from UI.Colors import *


class GamePanel:
    
    def __init__(self):
        self.log_subject = LogSubject()
        
        self.display_surface = pygame.display.set_mode((screen_width + log_width, screen_height))
        self.log_panel = LogPanel(screen_width, 0, log_width, log_height, pygame.font.SysFont("Arial", 18), pygame.font.SysFont("Arial", 18))
        self.log_subject.attach_log_observer(self.log_panel)

        pygame.display.set_caption("The Tower of Light")

    def play(self):
        
        game_map = TileManager()
        game_map.map_load()

        race, warrior = CharacterCreationPanel.create_character_creation_panel(self.display_surface)

        if race is None or warrior is None:
            MainMenu.create_main_menu(self.display_surface, self.play, pygame.event.get())
            return
        
        player = Player(player_spawn, race, warrior)
        warrior.init_starter_weapon(player)

        inventory = Inventory()

        item_manager = ItemManager()
        # healing_potion_1 = HealthPotion(MapPosition(8, 48))
        # healing_potion_2 = HealthPotion(MapPosition(10, 45))
        # mana_potion_1 = ManaPotion(MapPosition(9, 46))
        # item_manager.create_item(healing_potion_1)
        # item_manager.create_item(healing_potion_2)
        # item_manager.create_item(mana_potion_1)

        clock = pygame.time.Clock()

        running = True
        while running:
            events = pygame.event.get()
            
            for event in events:
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    player.motion(event, map_width, map_height, game_map.map_tiles)
                    player.actions(event, game_map, inventory.get_all_items(), inventory)


            item_manager.check_for_pickups(player, inventory)

            self.log_panel.log_scrolling(events)
            
            self.display_surface.fill(background_color)
            
            game_map.tile_vilibility(player)
            item_manager.item_visibility(player)

            game_map.draw_map(self.display_surface)

            main_menu_callback = lambda: MainMenu.create_main_menu(self.display_surface, self.play, pygame.event.get())
            if game_map.advance_level(player, self.display_surface, main_menu_callback):
                return

            # Draw the player
            pygame.draw.rect(self.display_surface, player_color, player.rect)
            pygame.draw.rect(self.display_surface, (0, 0, 0), player.rect, 1)

            # Draw the items
            item_manager.draw_item(self.display_surface)

            # Draw the log panel
            self.log_panel.draw(self.display_surface, player, inventory)

            # Update the display
            pygame.display.update()

            # Setting the frame rate
            clock.tick(60)