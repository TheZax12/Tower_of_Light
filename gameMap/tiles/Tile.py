from gameMap.tiles.types.FloorTile import FloorTile
from gameMap.tiles.types.WallTile import WallTile

class Tile:

    def __init__(self, object_position):
        self.object_position = object_position
        self.discovered = False
        self.visible = False

    @staticmethod
    def from_integer_to_tile(x, y, integer):
        """
        Create a tile from an integer
        :param x: The x coordinate of the tile
        :param y: The y coordinate of the tile
        :param integer: The integer value of the tile
        :return: A tile object
        """
        if integer == 1:
            return WallTile(x, y)
        elif integer == 0:
            return FloorTile(x, y)
        else:
            raise ValueError("Invalid tile integer")