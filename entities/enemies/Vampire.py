from math import inf

from entities.enemies.Enemy import Enemy
from gameMap.MapPosition import MapPosition
from items.equipables.weapons.Dagger import Dagger


class Vampire(Enemy):

    def __init__(self, position: MapPosition):
        super().__init__(position)
        
        self.set_name("Vampire")

        self.set_max_hitpoints(20)
        self.set_thrust_defence(0)
        self.set_swing_defence(0)
        self.set_magic_defence(inf)
        
        self.set_main_hand(Dagger(self.get_position()))
        
        self.set_experience_points(30)