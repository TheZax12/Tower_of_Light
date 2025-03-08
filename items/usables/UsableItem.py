from gameMap.MapPosition import MapPosition
from items.Item import Item

from UI.Colors import *


class UsableItem(Item):

    def __init__(self, position: MapPosition):
        super().__init__(position)
        self.visible_color = usable_tile_visible_color
        self.invisible_color = usable_tile_invisible_color