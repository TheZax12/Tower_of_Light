from enum import Enum

class TileType(Enum):
    """ Enum class to convert .txt files to objects of type tile. """
    FLOOR = 0
    WALL = 1

    @staticmethod
    def int_to_tile(x: int):
        for tile in TileType:
            if tile.value == x:
                return tile
        raise ValueError(f"No tile of that type found for integer {x}")
    