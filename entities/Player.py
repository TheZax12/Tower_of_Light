import pygame

from entities.Entity import Entity
from gameMap.MapSettings import MapSettings


class Player(Entity):

    def __init__(self):
        super().__init__()


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

        new_rect = pygame.Rect(new_tile_x * MapSettings.tile_size, new_tile_y * MapSettings.tile_size, MapSettings.tile_size, MapSettings.tile_size)
        
        return new_tile_x, new_tile_y, new_rect