from entities.enemies.Enemy import Enemy
from gameMap.MapPosition import MapPosition
from items.equipables.weapons.Staff import Staff


class Bishop(Enemy):
    
    def __init__(self, game_panel, position: MapPosition):
        super().__init__(game_panel, position)

        self.set_name("Bishop")

        self.set_max_hitpoints(40)
        self.set_hitpoints(self.get_max_hitpoints())
        self.set_thrust_defence(0)
        self.set_swing_defence(0)
        self.set_magic_defence(5)

        self.set_main_hand(Staff(self.get_position()))

        self.set_experience_points(60)

    def init_appearance_on_level(self):
        return [2, 3, 4]