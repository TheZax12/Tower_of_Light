from entities.enemies.Enemy import Enemy
from gameMap.MapPosition import MapPosition
from items.equipables.weapons.HammerOfWrath import HammerOfWrath


class Paladin(Enemy):

    def __init__(self, position: MapPosition):
        super().__init__(position)

        self.set_name("Paladin")

        self.set_max_hitpoints(100)
        self.set_thrust_defence(3)
        self.set_swing_defence(5)
        self.set_magic_defence(2)

        self.set_main_hand(HammerOfWrath(self.get_position()))

        self.set_experience_points(80)