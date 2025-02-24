import pygame

from main.GameWindow import GameWindow
from entities.Player import Player
from gameMap.tiles.TileType import TileType
from gameMap.tiles.Tile import Tile
from gameMap.MapPosition import MapPosition

from gameMap.MapSettings import *
from UI.Colors import *


class MapCreation:

    def __init__(self):
        self.map_tiles = [[Tile(None) for _ in range(map_width)] for _ in range(map_height)]
        
    def map_load(self, level_number):
        file_path = "gameMap/levels/level_" + str(level_number) + ".txt"
        
        with open(file_path, "r") as file:
            level_data = file.readlines()

        for row_index, row in enumerate(level_data):
            level_data_col = row.split(" ")
            for col_index, col in enumerate(level_data_col):
                tile_type = TileType.int_to_tile(int(col))
                self.map_tiles[row_index][col_index] = Tile.create_tile(tile_type, MapPosition(col_index, row_index))

    def tile_vilibility(self, player: Player):
        for row in self.map_tiles:
            for tile in row:
                distance_to_tile = tile.position.distance(player.get_position())
                if distance_to_tile <= player.visibility_radius:
                    tile.set_visible(True)
                    if not tile.is_discorvered():
                        tile.set_discovered(True)
                else:
                    tile.set_visible(False)

    def draw_map(self, display_surface):
        for row in self.map_tiles:
            for tile in row:
                if not tile.is_discorvered():
                    pygame.draw.rect(display_surface, undiscovered_area_color, (tile.position.x * tile_size, tile.position.y * tile_size, tile_size, tile_size))
                elif tile.is_visible():
                    pygame.draw.rect(display_surface, tile.visible_color, (tile.position.x * tile_size, tile.position.y * tile_size, tile_size, tile_size))
                else:
                    pygame.draw.rect(display_surface, tile.invisible_color, (tile.position.x * tile_size, tile.position.y * tile_size, tile_size, tile_size))

        
    def draw_grid(self, display_surface):
        for x in range(0, GameWindow.screen_width + tile_size, tile_size):
            pygame.draw.line(display_surface, grid_color, (x, 0), (x, GameWindow.screen_height))
        for y in range(0, GameWindow.screen_height + tile_size, tile_size):
            pygame.draw.line(display_surface, grid_color, (0, y), (GameWindow.screen_width, y))
