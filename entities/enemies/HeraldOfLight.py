from entities.enemies.Enemy import Enemy
from gameMap.MapPosition import MapPosition
from items.equipables.weapons.Lightbringer import Lightbringer


class HeraldOfLight(Enemy):

    def __init__(self, position: MapPosition):
        super().__init__(position)

        self.set_name("Herald of light")

        self.set_max_hitpoints(160)
        self.set_thrust_defence(2)
        self.set_swing_defence(2)
        self.set_magic_defence(2)

        self.set_main_hand(Lightbringer(self.get_position()))

        self.set_experience_points(400)