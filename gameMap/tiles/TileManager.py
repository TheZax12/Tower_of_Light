import pygame
from sys import maxsize

from gameMap.tiles.TileType import TileType
from gameMap.tiles.Tile import Tile
from gameMap.tiles.decorators.BeaconTile import BeaconTile
from gameMap.tiles.decorators.ExitTile import ExitTile
from gameMap.MapPosition import MapPosition
from log.LogSubject import LogSubject

from gameMap.MapSettings import *
from UI.Colors import *


class TileManager:

    def __init__(self, game_panel):
        self.game_panel = game_panel
        self.log_subject = LogSubject()
        
        self.map_tiles = [[Tile(None) for _ in range(map_width)] for _ in range(map_height)]
        self.wall_tiles = []
        self.beacon_tiles = []

        self.max_beacon_number = 3
        self.min_beacon_distance = 15

        self.map_load()

    def set_tile(self, position: MapPosition, tile: Tile):
        self.map_tiles[position.y][position.x] = tile

    def get_tile(self, position: MapPosition) -> Tile:
        return self.map_tiles[position.y][position.x]
        
    def map_load(self):
        file_path = "gameMap/levels/level_" + str(self.game_panel.get_game_level()) + ".txt"
        
        with open(file_path, "r") as file:
            level_data = file.readlines()

        for row_index, row in enumerate(level_data):
            level_data_col = row.split(" ")
            for col_index, col in enumerate(level_data_col):
                tile_type = TileType.int_to_tile(int(col))
                tile = Tile.create_tile(tile_type, MapPosition(col_index, row_index))
                self.map_tiles[row_index][col_index] = tile

                if tile.get_type() == TileType.WALL:
                    self.wall_tiles.append(tile)
    
    def get_wall_tiles(self):
        return self.wall_tiles
    
    def min_player_spawn_beacon_distance(self, position: MapPosition):
        return position.distance_to(player_spawn)
    
    def beacons_min_distance(self, position: MapPosition):
        return min((position.distance_to(beacon.get_position()) for beacon in self.beacon_tiles), default=maxsize)
    
    def add_beacon(self, position: MapPosition):
        if len(self.beacon_tiles) >= self.max_beacon_number:
            return
        beacon = BeaconTile(position)
        self.set_tile(beacon.get_position(), beacon)
        self.beacon_tiles.append(beacon)

        self.log_subject.notify_log_observer(f"Create {len(self.beacon_tiles)}/{self.max_beacon_number} beacons of light.")
        self.game_panel.enemy_manager.update_on_beacon_creation()

        if len(self.beacon_tiles) == self.max_beacon_number:
            self.convert_to_light()
            
    def convert_to_light(self):
        exit = ExitTile(exit_spawn)
        self.set_tile(exit.get_position(), exit)

        for row in self.map_tiles:
            for tile in row:
                tile.set_discovered(True)
                tile.chaos_to_light()

    def tile_visibility(self):
        player = self.game_panel.player
        
        for row in self.map_tiles:
            for tile in row:
                distance_to_tile = tile.get_position().distance_to(player.get_position())
                if distance_to_tile <= player.visibility_radius:
                    tile.set_visible(True)
                    if not tile.is_discovered():
                        tile.set_discovered(True)
                else:
                    tile.set_visible(False)

    def update(self):
        self.tile_visibility()

    def reset(self):
        self.beacon_tiles.clear()
        self.wall_tiles.clear()
        self.map_load()
        self.tile_visibility()

    def draw_map(self, display_surface: pygame.Surface):
        for row in self.map_tiles:
            for tile in row:
                tile.draw_tile(display_surface)
                pygame.draw.rect(display_surface, (0, 0, 0), (tile.position.get_tile_x(), tile.position.get_tile_y(), tile_size, tile_size), 1)