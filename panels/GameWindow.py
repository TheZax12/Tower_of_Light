import pygame
from sys import exit

from entities.player.Player import Player
from gameMap.tiles.TileManager import TileManager
from panels.MainMenu import MainMenu

from panels.PanelSettings import *
from gameMap.MapSettings import *
from UI.Colors import *


class GameWindow:
    
    def set_caption(self, caption: str):
        pygame.display.set_caption(caption)
    
    def create_display_surface(self):
        self.display_surface = pygame.display.set_mode((screen_width + log_size, screen_height))  

    def get_display_surface(self):
        return self.display_surface

    def play_game(self):

        game_map = TileManager()
        game_map.map_load()

        player = Player(southwest)

        clock = pygame.time.Clock()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    player.motion(event, map_width, map_height, game_map.map_tiles)
                    player.actions(event, game_map)

            self.display_surface.fill(background_color)
            
            game_map.tile_vilibility(player)

            game_map.draw_map(self.display_surface)

            main_menu_callback = lambda: MainMenu.create_main_menu(self.display_surface, pygame.event.get(), self.play_game)
            if game_map.advance_level(player, self.display_surface, main_menu_callback):
                return

            # Draw the player
            pygame.draw.rect(self.display_surface, player_color, player.rect)
            pygame.draw.rect(self.display_surface, (0, 0, 0), player.rect, 1)

            # Update the display
            pygame.display.update()

            # Setting the frame rate
            clock.tick(60)
