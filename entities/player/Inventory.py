from items.usables.HealthPotion import HealthPotion
from items.usables.ManaPotion import ManaPotion


class Inventory:

    def __init__(self, game_panel):
        self.game_panel = game_panel
        self.usable_items = []

    def get_usable_items(self):
        return self.usable_items
    
    def add_item(self, usable_item):
        self.usable_items.append(usable_item)

    def remove_used_items(self):
        for item in self.usable_items[:]:
            if item.get_uses_number() == 0:
                self.usable_items.remove(item)

    def get_item_type(self, item_type):
        return [item for item in self.usable_items if isinstance(item, item_type)]
    
    def get_number_of_items_of_type(self, item_type):
        return len(self.get_item_type(item_type))

    def get_number_of_uses_of_item_type(self, item_type):
        return sum(item.get_uses_number() for item in self.get_item_type(item_type))

    def inventory_contents(self):
        healing_potion_number = self.get_number_of_items_of_type(HealthPotion)
        healing_potion_uses = self.get_number_of_uses_of_item_type(HealthPotion)

        mana_potion_number = self.get_number_of_items_of_type(ManaPotion)
        mana_potion_uses = self.get_number_of_uses_of_item_type(ManaPotion)

        main_weapon = self.game_panel.player.get_main_hand().get_item_name() if self.game_panel.player.get_main_hand() else "None"
        secondary_weapon = self.game_panel.player.get_off_hand().get_item_name() if self.game_panel.player.get_off_hand() else "None"
        
        return (
            f"Main weapon: {main_weapon}\n"
            f"Secondary weapon: {secondary_weapon}\n"
            f"Healing potions: {healing_potion_number} ({healing_potion_uses} uses)\n"
            f"Mana potions: {mana_potion_number} ({mana_potion_uses} uses)"
        )