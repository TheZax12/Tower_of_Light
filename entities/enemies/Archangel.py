from entities.enemies.Enemy import Enemy
from gameMap.MapPosition import MapPosition
from items.equipables.weapons.DivineHammer import DivineHammer


class Archangel(Enemy):

    def __init__(self, game_panel, position: MapPosition):
        super().__init__(game_panel, position)

        self.set_name("Archangel")

        self.set_max_hitpoints(130)
        self.set_hitpoints(self.get_max_hitpoints())
        self.set_thrust_defence(6)
        self.set_swing_defence(6)
        self.set_magic_defence(2)

        self.set_main_hand(DivineHammer(self.get_position()))

        self.set_experience_points(120)

    def init_appearance_on_level(self):
        return [4, 5, 6]