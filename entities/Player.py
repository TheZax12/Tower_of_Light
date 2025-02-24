import pygame

from entities.Entity import Entity
from gameMap.MapPosition import MapPosition

from gameMap.MapSettings import *


class Player(Entity):

    def __init__(self, position: MapPosition):
        super().__init__(position)
        self.visibility_radius = 6
    
    def motion(self, event, player_tile_x, player_tile_y, map_width, map_height):
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
        
        return new_tile_x, new_tile_y, new_rect