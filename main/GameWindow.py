import pygame
from gameMap.MapSettings import MapSettings


class GameWindow:

    screen_width = MapSettings.map_width * MapSettings.tile_size
    screen_height = MapSettings.map_height * MapSettings.tile_size

    def __init__(self, window_width, window_height, log_size):
        self.window_width = window_width
        self.window_height = window_height
        self.log_size = log_size

    def calculate_scaling(self):
        scaling_factor = min(self.window_width / self.screen_width, self.window_height / self.screen_height)
        scaled_tile_size = int(MapSettings.tile_size * scaling_factor)
        scaled_screen_width = MapSettings.map_width * scaled_tile_size
        scaled_screen_height = MapSettings.map_height * scaled_tile_size
        return scaling_factor, scaled_tile_size, scaled_screen_width, scaled_screen_height

    def create_display_surface(self):
        scaling_factor, scaled_tile_size, scaled_screen_width, scaled_screen_height = self.calculate_scaling()
        display_surface = pygame.display.set_mode((scaled_screen_width + self.log_size, scaled_screen_height))
        pygame.display.set_caption('Tower of Light')
        return display_surface

