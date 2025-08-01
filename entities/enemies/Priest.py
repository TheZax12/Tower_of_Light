import math

from entities.enemies.Enemy import Enemy
from gameMap.MapPosition import MapPosition
from items.equipables.weapons.Mace import Mace


class Priest(Enemy):

    def __init__(self, game_panel, position: MapPosition):
        super().__init__(game_panel, position)
        
        self.set_name("Priest")

        self.set_max_hitpoints(20)
        self.set_hitpoints(self.get_max_hitpoints())
        self.set_thrust_defence(0)
        self.set_swing_defence(0)
        self.set_magic_defence(math.inf)

        self.set_main_hand(Mace(self.get_position()))
        
        self.set_experience_points(30)

    def init_appearance_on_level(self):
        return [1, 2]