tile_size = 16
""" The size of each tile in pixels """

map_width = 52
""" The number of tiles in the width of the map """

map_height = 52
""" The number of tiles in the height of the map """

item_size = 7
""" The size of the items on the map in pixels """

from gameMap.MapPosition import MapPosition

southwest = MapPosition.generate_position(2, map_height - 3)
""" The southwest corner of the map, where the player starts """

northeast = MapPosition.generate_position(map_width - 3, 2)
""" The northeast corner of the map, where the exit is located """