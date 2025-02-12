from gameMap.MapSettings import MapSettings


class MapPosition():

    def __init__(self, x_pixel, y_pixel):
        """
        Create a position on the map
        :param x_pixel: The x coordinate in pixels
        :param y_pixel: The y coordinate in pixels
        """
        self.x_pixel = x_pixel
        self.y_pixel = y_pixel
        self.x_tile = x_pixel * MapSettings.tile_size
        self.y_tile = y_pixel * MapSettings.tile_size

    @staticmethod
    def new_position(x, y):
        """
        Responsible for creating a new position on the map, taking into account the map limits.
        :param x: The x coordinate on the grid
        :param y: The y coordinate on the grid
        :return: The new position
        """
        if x >= MapSettings.map_width:
            x = MapSettings.map_width - 1
        elif x < 0:
            x = 1

        if y >= MapSettings.map_height:
            y = MapSettings.map_height - 1
        elif y < 0:
            y = 1

        return MapPosition(x, y)

    def get_x_pos_tile(self):
        """
        Gets the x position of the object on the grid
        :return: The x position
        """
        return self.x_tile

    def get_x_pos_pixel(self):
        """
        Gets the x position in pixels
        :return: The x position
        """
        return self.x_pixel

    def get_y_pos_tile(self):
        """
        Gets the y position of the object on the grid
        :return: The y position
        """
        return self.y_tile

    def get_y_pos_pixel(self):
        """
        Gets the y position in pixels
        :return: The y position
        """
        return self.y_pixel

    