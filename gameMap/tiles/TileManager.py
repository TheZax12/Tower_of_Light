import pygame
from sys import maxsize

from gameMap.tiles.TileType import TileType
from gameMap.tiles.Tile import Tile
from gameMap.tiles.decorators.BeaconTile import BeaconTile
from gameMap.tiles.decorators.ExitTile import ExitTile
from gameMap.MapPosition import MapPosition

from gameMap.MapSettings import *
from UI.Colors import *


class TileManager:

    def __init__(self):
        self.map_tiles = [[Tile(None) for _ in range(map_width)] for _ in range(map_height)]
        self.beacon_tiles = []

        self.max_beacon_number = 3
        self.min_beacon_distance = 15

    def set_tile(self, position: MapPosition, tile: Tile):
        self.map_tiles[position.y][position.x] = tile

    def get_tile(self, position: MapPosition) -> Tile:
        return self.map_tiles[position.y][position.x]
        
    def map_load(self, level_number):
        file_path = "gameMap/levels/level_" + str(level_number) + ".txt"
        
        with open(file_path, "r") as file:
            level_data = file.readlines()

        for row_index, row in enumerate(level_data):
            level_data_col = row.split(" ")
            for col_index, col in enumerate(level_data_col):
                tile_type = TileType.int_to_tile(int(col))
                self.map_tiles[row_index][col_index] = Tile.create_tile(tile_type, MapPosition(col_index, row_index))

    def beacons_min_distance(self, position: MapPosition):
        return min((position.distance(beacon.get_position()) for beacon in self.beacon_tiles), default=maxsize)
    
    def add_beacon(self, position: MapPosition):
        if len(self.beacon_tiles) >= self.max_beacon_number:
            print("No more beacons can be placed")
        beacon = BeaconTile(position)
        self.set_tile(beacon.get_position(), beacon)
        self.beacon_tiles.append(beacon)

        if len(self.beacon_tiles) == self.max_beacon_number:
            self.convert_to_light()
            
    def convert_to_light(self):
        exit = ExitTile(northeast)
        self.set_tile(exit.get_position(), exit)

        for row in self.map_tiles:
            for tile in row:
                tile.set_discovered(True)
                tile.chaos_to_light()

    def tile_vilibility(self, player):
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
                
                pygame.draw.rect(display_surface, (0, 0, 0), (tile.position.x * tile_size, tile.position.y * tile_size, tile_size, tile_size), 1)

    def reset(self):
        self.beacon_tiles = []
        self.tile_vilibility()
