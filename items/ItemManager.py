from log.LogSubject import LogSubject
from items.equipables.EquipableItem import EquipableItem
from items.usables.UsableItem import UsableItem

class ItemManager:

    def __init__(self, game_panel):
        self.game_panel = game_panel

        self.equipable_items = {}
        self.usable_items = {}

        self.last_player_position = None

    def get_all_items(self):
        all_items = []
        for item_list in self.equipable_items.values():
            all_items.extend(item_list)
        for item_list in self.usable_items.values():
            all_items.extend(item_list)
        return all_items

    def create_item(self, item):
        position = item.get_position()
        if isinstance(item, EquipableItem):
            self.equipable_items.setdefault(position, []).append(item)
        elif isinstance(item, UsableItem):
            self.usable_items.setdefault(position, []).append(item)

    def erase_item(self, item):
        position = item.get_position()
        if isinstance(item, EquipableItem):
            items = self.equipable_items.get(position)
            if items and item in items:
                items.remove(item)
                if not items:
                    del self.equipable_items[position]
        elif isinstance(item, UsableItem):
            items = self.usable_items.get(position)
            if items and item in items:
                items.remove(item)
                if not items:
                    del self.usable_items[position]

    def usable_item_auto_pickup(self):
        """Check if the player is on the same tile as an usable item and add it to the inventory."""
        log_subject = LogSubject()

        position = self.game_panel.player.get_position()
        items = self.usable_items.get(position, [])[:]
        for item in items:
            self.game_panel.inventory.add_item(item)
            log_subject.notify_log_observer(f"Picked up a {item.get_item_name()}.")
            self.erase_item(item)
    
    def equipment_on_tile(self):
        """Notify the player about the equipable items on the tile they are currently on."""
        log_subject = LogSubject()

        current_position = self.game_panel.player.get_position()
        if current_position == self.last_player_position:
            return
        
        if not self.equipable_items:
            return

        equipment_on_tile = self.equipable_items.get(current_position, [])
        if equipment_on_tile:
            log_subject.notify_log_observer("Piece of equipment on tile:")
            for idx, item in enumerate(equipment_on_tile, 1):
                log_subject.notify_log_observer(f"{idx}. {item.get_item_name()}")

    def item_visibility(self):
        for item in self.get_all_items():
            item.visibility(self.game_panel.player)

    def update(self):
        self.item_visibility()
        self.usable_item_auto_pickup()
        self.equipment_on_tile()
        self.last_player_position = self.game_panel.player.get_position()

    def reset(self):
        self.equipable_items.clear()
        self.usable_items.clear()

    def restart(self):
        self.reset()

    def draw_items(self, display_surface):
        for item in self.get_all_items():
            item.draw(display_surface)
