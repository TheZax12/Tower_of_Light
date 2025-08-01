from entities.enemies.Enemy import Enemy
from gameMap.MapPosition import MapPosition
from items.equipables.weapons.BladeOfLight import BladeOfLight


class Knight(Enemy):

    def __init__(self, game_panel, position: MapPosition):
        super().__init__(game_panel, position)

        self.set_name("Knight")

        self.set_max_hitpoints(30)
        self.set_hitpoints(self.get_max_hitpoints())
        self.set_thrust_defence(3)
        self.set_swing_defence(3)
        self.set_magic_defence(1)

        self.set_main_hand(BladeOfLight(self.get_position()))

        self.set_experience_points(50)

    def init_appearance_on_level(self):
        return [2, 3, 4]