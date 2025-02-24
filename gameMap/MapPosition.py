from __future__ import annotations

from gameMap.MapSettings import *


class MapPosition:
    
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.x_tile = x * tile_size
        self.y_tile = y * tile_size

    def get_x(self) -> int:
        return self.x
    
    def get_y(self) -> int:
        return self.y
    
    def distance(self, other: MapPosition) -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)