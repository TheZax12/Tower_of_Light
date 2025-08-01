from __future__ import annotations


class MapPosition:
    
    def __init__(self, x: int, y: int):
        from gameMap.MapSettings import tile_size
        self.x = x
        self.y = y
        self.tile_x = x * tile_size
        self.tile_y = y * tile_size

    def __eq__(self, other):
        if not isinstance(other, MapPosition):
            return NotImplemented
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def get_x(self) -> int:
        return self.x
    
    def get_y(self) -> int:
        return self.y
    
    def get_tile_x(self) -> int:
        return self.tile_x

    def get_tile_y(self) -> int:
        return self.tile_y
    
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
    
    def above(self) -> MapPosition:
        return self.generate_position(self.x, self.y - 1)
    
    def below(self) -> MapPosition:
        return self.generate_position(self.x, self.y + 1)
    
    def left(self) -> MapPosition:
        return self.generate_position(self.x - 1, self.y)
    
    def right(self) -> MapPosition:
        return self.generate_position(self.x + 1, self.y)

    def distance_to(self, other: MapPosition) -> int:
        """Calculates the Manhattan distance to another position."""
        return abs(self.x - other.x) + abs(self.y - other.y)