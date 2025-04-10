import pygame
from sys import exit

from entities.player.Player import Player
from gameMap.tiles.TileManager import TileManager
from panels.MainMenu import MainMenu
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

        player = Player(southwest)

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
                    player.actions(event, game_map)

            self.log_panel.log_scrolling(events)
            
            self.display_surface.fill(background_color)
            
            game_map.tile_vilibility(player)

            game_map.draw_map(self.display_surface)

            main_menu_callback = lambda: MainMenu.create_main_menu(self.display_surface, pygame.event.get(), self.play)
            if game_map.advance_level(player, self.display_surface, main_menu_callback):
                return

            # Draw the player
            pygame.draw.rect(self.display_surface, player_color, player.rect)
            pygame.draw.rect(self.display_surface, (0, 0, 0), player.rect, 1)

            self.log_panel.draw(self.display_surface)

            # Update the display
            pygame.display.update()

            # Setting the frame rate
            clock.tick(60)