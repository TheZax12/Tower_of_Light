import pygame

from entities.Entity import Entity
from gameMap.tiles.TileManager import TileManager
from gameMap.MapPosition import MapPosition

from gameMap.MapSettings import *


class Player(Entity):

    def __init__(self, position: MapPosition):
        super().__init__(position)
        self.visibility_radius = 6
        self.rect = pygame.Rect(self.get_position().x * tile_size, 
                                self.get_position().y * tile_size, 
                                tile_size, tile_size)

    def update_rect(self):
        self.rect.topleft = (self.get_position().x * tile_size, self.get_position().y * tile_size)

    def motion(self, event, map_width, map_height, map_tiles):
        current = self.get_position()
        new_tile_x, new_tile_y = current.x, current.y
        if event.key == pygame.K_w and current.y > 0:
            new_tile_y -= 1
        elif event.key == pygame.K_s and current.y < map_height - 1:
            new_tile_y += 1
        elif event.key == pygame.K_a and current.x > 0:
            new_tile_x -= 1
        elif event.key == pygame.K_d and current.x < map_width - 1:
            new_tile_x += 1

        new_rect = pygame.Rect(new_tile_x * tile_size, new_tile_y * tile_size, tile_size, tile_size)

        if not self.check_collision(new_rect, map_tiles):
            self.set_position(MapPosition(new_tile_x, new_tile_y))
            self.update_rect()

    def actions(self, event, tile_manager: TileManager):
        min_distance = tile_manager.beacons_min_distance(self.get_position())
        if event.key == pygame.K_l:
            if min_distance >= tile_manager.min_beacon_distance:
                tile_manager.add_beacon(self.get_position())
            else:
                print("Too close to another beacon")

    def reset(self):
        self.set_position(southwest)
        self.update_rect()