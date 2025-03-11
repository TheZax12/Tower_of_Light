from __future__ import annotations


class MapPosition:
    
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_x(self) -> int:
        return self.x
    
    def get_y(self) -> int:
        return self.y
    
    def distance(self, other: MapPosition) -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)
    
    @staticmethod
    def generate_position(x: int, y: int) -> MapPosition:
        from gameMap.MapSettings import map_height, map_width
        
        if x >= map_width:
            x = map_width - 1
        elif x < 0:
            x = 0
        
        if y >= map_height:
            y = map_height - 1
        elif y < 0:
            y = 0
        
        return MapPosition(x, y)