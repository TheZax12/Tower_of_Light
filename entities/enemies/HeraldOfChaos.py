from entities.enemies.Enemy import Enemy
from gameMap.MapPosition import MapPosition
from items.equipables.weapons.EdgeOfChaos import EdgeOfChaos


class HeraldOfChaos(Enemy):

    def __init__(self, position: MapPosition):
        super().__init__(position)

        self.set_name("Herald of chaos")

        self.set_max_hitpoints(160)
        self.set_thrust_defence(2)
        self.set_swing_defence(2)
        self.set_magic_defence(2)

        self.set_main_hand(EdgeOfChaos(self.get_position()))

        self.set_experience_points(400)