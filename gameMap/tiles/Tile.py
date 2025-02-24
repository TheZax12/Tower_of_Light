from gameMap.MapPosition import MapPosition
from gameMap.tiles.TileType import TileType

from UI.Colors import *


class Tile:

    def __init__(self, position: MapPosition, tile_type=None):
        self.position = position
        self.tile_type = tile_type
        self.discovered = False
        self.visible = False

    @staticmethod
    def create_tile(tile_type: TileType, position: MapPosition):
        from gameMap.tiles.types.FloorTile import FloorTile
        from gameMap.tiles.types.WallTile import WallTile
        if tile_type == TileType.FLOOR: return FloorTile(position)
        if tile_type == TileType.WALL: return WallTile(position)

    def get_position(self) -> MapPosition:
        return self.position

    def set_discovered(self, discovered: bool):
        self.discovered = discovered
    
    def is_discorvered(self) -> bool:
        return self.discovered
    
    def set_visible(self, visible: bool):    
        self.visible = visible
    
    def is_visible(self) -> bool:
        return self.visible
    
    def set_visible_color(self, color):
        self.visible_color = color

    def set_invisible_color(self, color):
        self.invisible_color = color

    def get_type(self) -> TileType:
        return self.tile_type

    def chaos_to_light(self):
        pass
    