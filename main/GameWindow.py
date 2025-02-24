import pygame

from gameMap.MapSettings import *


class GameWindow:

    screen_width = map_width * tile_size
    screen_height = map_height * tile_size

    def __init__(self, window_width, window_height, log_size):
        self.window_width = window_width
        self.window_height = window_height
        self.log_size = log_size

    def create_display_surface(self):
        display_surface = pygame.display.set_mode((self.screen_width + self.log_size, self.screen_height))
        return display_surface

