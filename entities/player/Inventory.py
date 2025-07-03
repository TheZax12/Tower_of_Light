from items.usables.UsableItem import UsableItem
from items.usables.ManaPotion import ManaPotion
from items.usables.HealthPotion import HealthPotion


class Inventory:

    def __init__(self):
        self.healing_potion_inventory = []
        self.mana_potion_inventory = []

    def get_all_items(self):
        return self.healing_potion_inventory + self.mana_potion_inventory

    def add_item(self, usable_item):
        if isinstance(usable_item, HealthPotion): 
            self.healing_potion_inventory.append(usable_item)
            # usable_item.set_uses_number(usable_item.get_uses_number() + usable_item.init_uses_number())
        elif isinstance(usable_item, ManaPotion):
            self.mana_potion_inventory.append(usable_item)
            # usable_item.set_uses_number(usable_item.get_uses_number() + usable_item.init_uses_number())

    def remove_item(self, usable_item: UsableItem):
        if usable_item.get_uses_number() == 0:
            if isinstance(usable_item, HealthPotion):
                self.healing_potion_inventory.remove(usable_item)
            elif isinstance(usable_item, ManaPotion):
                self.mana_potion_inventory.remove(usable_item)

    def inventory_contents(self):
        healing_potion_uses = sum(item.get_uses_number() for item in self.healing_potion_inventory)
        mana_potion_uses = sum(item.get_uses_number() for item in self.mana_potion_inventory)
        
        return (
            f"Healing potions: {len(self.healing_potion_inventory)} ({healing_potion_uses} uses)\n"
            f"Mana potions: {len(self.mana_potion_inventory)} ({mana_potion_uses} uses)"
        )