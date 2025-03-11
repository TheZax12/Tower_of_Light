from gameMap.MapPosition import MapPosition
from gameMap.tiles.TileType import TileType
from gameMap.tiles.Tile import Tile

from UI.Colors import *


class WallTile(Tile):

    def __init__(self, position: MapPosition):
        super().__init__(position)
        self.tile_type = TileType.WALL
        self.set_visible_color(chaos_wall_tile_visible_color)
        self.set_invisible_color(chaos_wall_tile_invisible_color)

    def chaos_to_light(self):
        self.set_visible_color(light_wall_tile_visible_color)
        self.set_invisible_color(light_wall_tile_invisible_color)