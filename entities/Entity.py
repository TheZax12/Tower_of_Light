import pygame

from gameMap.tiles.TileType import TileType
from gameMap.MapPosition import MapPosition

from gameMap.MapSettings import *


class Entity():

    def __init__(self, position: MapPosition):
        self.position = position
        
    def set_position(self, position: MapPosition):
        self.position = position

    def get_position(self) -> MapPosition:
        return self.position
    
    def set_hitpoints(self, hitpoints: int):
        self.hitpoints = hitpoints

    def get_hitpoints(self) -> int:
        return self.hitpoints
    
    def set_max_hitpoints(self, max_hitpoints: int):
        self.max_hitpoints = max_hitpoints

    def get_max_hitpoints(self) -> int:
        return self.max_hitpoints

    def check_collision(self, new_rect, tiles):
        for row in tiles:
            for tile in row:
                if tile.get_type() == TileType.WALL:
                    tile_rect = pygame.Rect(tile.position.x * tile_size, tile.position.y * tile_size, tile_size, tile_size)
                    if new_rect.colliderect(tile_rect):
                        return True
        return False