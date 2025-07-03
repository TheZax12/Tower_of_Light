from entities.enemies.Enemy import Enemy
from gameMap.MapPosition import MapPosition
from items.equipables.weapons.DemonClaws import DemonClaws


class Fiend(Enemy):

    def __init__(self, position: MapPosition):
        super().__init__(position)

        self.set_name("Fiend")

        self.set_max_hitpoints(130)
        self.set_thrust_defence(6)
        self.set_swing_defence(6)
        self.set_magic_defence(2)

        self.set_main_hand(DemonClaws(self.get_position()))

        self.set_experience_points(200)