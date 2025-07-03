from copy import deepcopy

from items.equipables.EquipableItem import EquipableItem
from items.ItemEffect import ItemEffect
from gameMap.MapPosition import MapPosition
from items.equipables.Damage import Damage


class Weapon(EquipableItem):
    
    def __init__(self, position: MapPosition, item_effects: ItemEffect, damage_list: list[Damage], item_name: str):
        super().__init__(position, item_effects, item_name)
        self.damage_list = damage_list

    def get_damage_list(self) -> list[Damage]:
        return [deepcopy(damage) for damage in self.damage_list]