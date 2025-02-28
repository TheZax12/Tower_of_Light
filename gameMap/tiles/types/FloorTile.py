from gameMap.MapPosition import MapPosition
from gameMap.tiles.TileType import TileType
from gameMap.tiles.Tile import Tile

from UI.Colors import *


class FloorTile(Tile):

    def __init__(self, position: MapPosition):
        super().__init__(position)
        self.tile_type = TileType.FLOOR
        self.invisible_color = chaos_floor_tile_invisible_color
        self.visible_color = chaos_floor_tile_visible_color
        