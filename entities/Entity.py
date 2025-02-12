import pygame

from gameMap.MapPosition import MapPosition


class Entity():

    def __init__(self):
        pass

    def set_position(self, position: MapPosition):
        self.position = position

    def check_collision(self, new_rect, tiles):
        for tile_type, tile_rect in tiles:
            if tile_type == "wall" and new_rect.colliderect(tile_rect):
                return True
        return False