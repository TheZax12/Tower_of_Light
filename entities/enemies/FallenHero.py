from entities.enemies.Enemy import Enemy
from gameMap.MapPosition import MapPosition
from items.equipables.weapons.EbonBlade import EbonBlade


class FallenHero(Enemy):

    def __init__(self, game_panel, position: MapPosition):
        super().__init__(game_panel, position)

        self.set_name("Fallen Hero")

        self.set_max_hitpoints(100)
        self.set_hitpoints(self.get_max_hitpoints())
        self.set_thrust_defence(3)
        self.set_swing_defence(5)
        self.set_magic_defence(2)

        self.set_main_hand(EbonBlade(self.get_position()))

        self.set_experience_points(80)

    def init_appearance_on_level(self):
        return [3, 4, 5]