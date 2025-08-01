import pygame
from sys import exit

from entities.player.Player import Player
from entities.player.Inventory import Inventory
from gameMap.tiles.TileManager import TileManager
from items.ItemManager import ItemManager
from entities.enemies.EnemyManager import EnemyManager
from log.LogSubject import LogSubject
from panels.LogPanel import LogPanel

from panels.PanelSettings import *
from gameMap.MapSettings import *
from UI.Colors import *


class GamePanel:
    
    def __init__(self, display_surface, race, warrior):        
        self.display_surface = display_surface

        self.win = False
        self.game_over = False
        self.level_number = 1
        self.max_level_number = 6

        self.log_panel = LogPanel(self, screen_width, 0, log_width, log_height, pygame.font.SysFont("Arial", 18), pygame.font.SysFont("Arial", 18))
        self.log_subject = LogSubject()

        self.player = Player(self, player_spawn, race, warrior)
        self.inventory = Inventory(self)

        self.tile_manager = TileManager(self)
        self.enemy_manager = EnemyManager(self)
        self.item_manager = ItemManager(self)
        
        self.log_subject.attach_log_observer(self.log_panel)

    def set_win(self, win):
        self.win = win

    def is_win(self):
        return self.win
    
    def set_game_over(self, game_over):
        self.game_over = game_over

    def is_game_over(self):
        return self.game_over
    
    def set_game_level(self, level_number):
        self.level_number = level_number

    def get_game_level(self):
        return self.level_number
    
    def advance_level(self):            
            curernt_position = self.player.get_position()
            if curernt_position == exit_spawn and len(self.tile_manager.beacon_tiles) == self.tile_manager.max_beacon_number:
                if self.get_game_level() < self.max_level_number:
                    self.set_game_level(self.get_game_level() + 1)
                    self.reset()
                    self.log_subject.notify_log_observer(f"Advanced to level {self.get_game_level()}.")
                else:
                    self.set_win(True)

    def update(self):
        self.tile_manager.update()
        self.item_manager.update()
        if self.player.get_take_turn():
            self.enemy_manager.update()
            self.player.set_take_turn(False)

    def reset(self):
        self.player.reset_position()
        self.tile_manager.reset()
        self.item_manager.reset()
        self.enemy_manager.reset()
        self.log_panel.reset()

    def draw(self):
        self.log_panel.draw(self.display_surface)
        self.tile_manager.draw_map(self.display_surface)
        self.player.draw(self.display_surface)
        self.enemy_manager.draw_enemies(self.display_surface)
        self.item_manager.draw_items(self.display_surface)
    
    def play(self, events):

        for event in events:
            if event.type == pygame.KEYDOWN:
                self.player.actions(event)
                self.player.update_level()

        self.display_surface.fill(background_color)

        self.log_panel.log_scrolling(events)
        
        self.update()
        self.advance_level()
        self.draw()

    def draw_game_state(self):
        self.display_surface.fill(background_color)
        self.draw()