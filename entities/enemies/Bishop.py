from entities.enemies.Enemy import Enemy
from gameMap.MapPosition import MapPosition
from items.equipables.weapons.Staff import Staff


class Bishop(Enemy):
    
    def __init__(self, position: MapPosition):
        super().__init__(position)

        self.set_name("Bishop")

        self.set_max_hitpoints(40)
        self.set_thrust_defence(0)
        self.set_swing_defence(0)
        self.set_magic_defence(5)

        self.set_main_hand(Staff(self.get_position()))

        self.set_experience_points(60)