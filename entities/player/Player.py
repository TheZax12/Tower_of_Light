import pygame

from entities.Entity import Entity
from gameMap.tiles.TileManager import TileManager
from gameMap.MapPosition import MapPosition
from log.LogSubject import LogSubject

from gameMap.MapSettings import *


class Player(Entity):

    def __init__(self, position: MapPosition):
        super().__init__(position)
        self.visibility_radius = 6
        self.rect = pygame.Rect(self.get_position().x * tile_size, 
                                self.get_position().y * tile_size, 
                                tile_size, tile_size)
        
    def set_level(self, level: int):
        self.level = level

    def get_level(self) -> int:
        return self.level
    
    def set_manapoints(self, manapoints: int):
        self.manapoints = manapoints

    def get_manapoints(self) -> int:
        return self.manapoints
    
    def set_max_manapoints(self, max_manapoints: int):
        self.max_manapoints = max_manapoints

    def get_max_manapoints(self) -> int:
        return self.max_manapoints
    
    def set_strength(self, strength: int):
        self.strength = strength

    def get_strength(self) -> int:
        return self.strength
    
    def set_intelect(self, intellect: int):
        self.intellect = intellect

    def get_intellect(self) -> int:
        return self.intellect

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
        log_subject = LogSubject()
        
        min_distance = tile_manager.beacons_min_distance(self.get_position())

        if event.key == pygame.K_l:
            if len(tile_manager.beacon_tiles) < tile_manager.max_beacon_number:
                if min_distance >= tile_manager.min_beacon_distance:
                        tile_manager.add_beacon(self.get_position())
                else:
                        log_subject.notify_log_observer("Too close to another beacon.")
            else:
                log_subject.notify_log_observer("Maximum number of beacons reached.")

    def reset(self):
        self.set_position(southwest)
        self.update_rect()