import pygame

from entities.Entity import Entity
from gameMap.tiles.TileManager import TileManager
from gameMap.MapPosition import MapPosition

from gameMap.MapSettings import *


class Player(Entity):

    def __init__(self, position: MapPosition):
        super().__init__(position)
        self.visibility_radius = 6
    
    def motion(self, event, player_tile_x, player_tile_y, map_width, map_height, map_tiles):
        new_tile_x, new_tile_y = player_tile_x, player_tile_y
        if event.key == pygame.K_w and player_tile_y > 0:
            new_tile_y -= 1
        elif event.key == pygame.K_s and player_tile_y < map_height - 1:
            new_tile_y += 1
        elif event.key == pygame.K_a and player_tile_x > 0:
            new_tile_x -= 1
        elif event.key == pygame.K_d and player_tile_x < map_width - 1:
            new_tile_x += 1

        new_rect = pygame.Rect(new_tile_x * tile_size, new_tile_y * tile_size, tile_size, tile_size)

        if not self.check_collision(new_rect, map_tiles):
                self.set_position(MapPosition(new_tile_x, new_tile_y))
                player_tile_x, player_tile_y = new_tile_x, new_tile_y
                new_rect.topleft = (player_tile_x * tile_size, player_tile_y * tile_size)

    def actions(self, event, tile_manager: TileManager):
        min_distance = tile_manager.beacons_min_distance(self.get_position())
        if event.key == pygame.K_l:
            if min_distance >= tile_manager.min_beacon_distance:
                tile_manager.add_beacon(self.get_position())
            elif min_distance < tile_manager.min_beacon_distance:
                print("Too close to another beacon")