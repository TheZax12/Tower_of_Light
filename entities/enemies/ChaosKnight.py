from entities.enemies.Enemy import Enemy
from gameMap.MapPosition import MapPosition
from items.equipables.weapons.SwordOfChaos import SwordOfChaos


class ChaosKnight(Enemy):

    def __init__(self, position: MapPosition):
        super().__init__(position)

        self.set_name("Chaos Knight")

        self.set_max_hitpoints(30)
        self.set_thrust_defence(3)
        self.set_swing_defence(3)
        self.set_magic_defence(1)

        self.set_main_hand(SwordOfChaos(self.get_position()))

        self.set_experience_points(50)