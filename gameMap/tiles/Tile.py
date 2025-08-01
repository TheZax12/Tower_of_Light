import pygame

from gameMap.MapPosition import MapPosition
from gameMap.tiles.TileType import TileType

from gameMap.MapSettings import tile_size
from UI.Colors import *


class Tile:

    def __init__(self, position: MapPosition):
        self.position = position
        self.discovered = False
        self.visible = False

    def set_position(self, positition: MapPosition):
        self.position = positition
    
    def get_position(self) -> MapPosition:
        return self.position
    
    def set_rect(self, rect: pygame.Rect):
        self.rect = rect

    def get_rect(self) -> pygame.Rect:
        return self.rect

    def set_collision(self, collision: bool):
        self.collision = collision

    def get_collision(self) -> bool:
        return self.collision
    
    def set_type(self, tile_type: TileType):
        self.tile_type = tile_type

    def get_type(self) -> TileType:
        return self.tile_type
    
    def is_walkable(self):
        return self.get_type() != TileType.WALL

    def set_discovered(self, discovered: bool):
        self.discovered = discovered
    
    def is_discovered(self) -> bool:
        return self.discovered
    
    def set_visible(self, visible: bool):    
        self.visible = visible
    
    def is_visible(self) -> bool:
        return self.visible
    
    def set_visible_color(self, color):
        self.visible_color = color

    def set_invisible_color(self, color):
        self.invisible_color = color

    @staticmethod
    def create_tile(tile_type, position: MapPosition):
        from gameMap.tiles.types.FloorTile import FloorTile
        from gameMap.tiles.types.WallTile import WallTile
        if tile_type == TileType.FLOOR: return FloorTile(position)
        if tile_type == TileType.WALL: return WallTile(position)
        
    def chaos_to_light(self):
        pass
    
    def draw_undiscovered(self, display_surface: pygame.Surface):
        self.set_rect(pygame.Rect(self.get_position().get_tile_x(), self.get_position().get_tile_y(), tile_size, tile_size))
        pygame.draw.rect(display_surface, undiscovered_area_color, self.get_rect())
    
    def draw_visible(self, display_surface: pygame.Surface):
        self.set_rect(pygame.Rect(self.get_position().get_tile_x(), self.get_position().get_tile_y(), tile_size, tile_size))
        pygame.draw.rect(display_surface, self.visible_color, self.get_rect())

    def draw_invisible(self, display_surface: pygame.Surface):
        self.set_rect(pygame.Rect(self.get_position().get_tile_x(), self.get_position().get_tile_y(), tile_size, tile_size))
        pygame.draw.rect(display_surface, self.invisible_color, self.get_rect())

    def draw_tile(self, display_surface: pygame.Surface):
        if not self.is_discovered():
            self.draw_undiscovered(display_surface)
        elif self.is_visible():
            self.draw_visible(display_surface)
        else:
            self.draw_invisible(display_surface)