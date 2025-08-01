from entities.enemies.Enemy import Enemy
from gameMap.MapPosition import MapPosition
from items.equipables.weapons.DemonClaws import DemonClaws


class Fiend(Enemy):

    def __init__(self, game_panel, position: MapPosition):
        super().__init__(game_panel, position)

        self.set_name("Fiend")

        self.set_max_hitpoints(130)
        self.set_hitpoints(self.get_max_hitpoints())
        self.set_thrust_defence(6)
        self.set_swing_defence(6)
        self.set_magic_defence(2)

        self.set_main_hand(DemonClaws(self.get_position()))

        self.set_experience_points(200)

    def init_appearance_on_level(self):
        return [5, 6]