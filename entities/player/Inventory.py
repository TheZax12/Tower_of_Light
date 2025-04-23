from items.usables.UsableItem import UsableItem
from items.usables.ManaPotion import ManaPotion
from items.usables.HealthPotion import HealthPotion


class Inventory:

    def __init__(self):
        self.healing_potion_inventory = []
        self.mana_potion_inventory = []

        self.healing_potion_uses = 0
        self.mana_potion_uses = 0

    def add_item(self, usable_item):        
        if isinstance(usable_item, HealthPotion): 
            self.healing_potion_inventory.append(usable_item)
            self.healing_potion_uses += usable_item.get_uses_number()
        elif isinstance(usable_item, ManaPotion):
            self.mana_potion_inventory.append(usable_item)
            self.mana_potion_uses += usable_item.get_uses_number()

    def inventory_contents(self):
        return (
            f"Healing potions: {len(self.healing_potion_inventory)} ({self.healing_potion_uses} uses)\n"
            f"Mana potions: {len(self.mana_potion_inventory)} ({self.mana_potion_uses} uses)"
        )