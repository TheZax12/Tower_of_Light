from gameMap.tiles.Tile import Tile
from gameMap.MapPosition import MapPosition

from UI.Colors import *


class ExitTile(Tile):

    def __init__(self, position: MapPosition):
        super().__init__(position)
        self.tile_type = None
        self.set_visible_color(exit_tile_visible_color)
        self.set_invisible_color(exit_tile_invisible_color)