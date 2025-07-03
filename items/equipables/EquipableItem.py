from gameMap.MapPosition import MapPosition
from items.Item import Item
from items.ItemEffect import ItemEffect

from UI.Colors import *


class EquipableItem(Item):

    def __init__(self, position: MapPosition, item_effects: ItemEffect, item_name: str):
        super().__init__(position)
        self.visible_color = equipable_tile_visible_color
        self.invisible_color = equipable_tile_invisible_color

        self.item_name = item_name
        self.item_effects = item_effects

    def init_item_effects(self):
        pass