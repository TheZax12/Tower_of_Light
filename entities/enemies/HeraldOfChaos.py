from entities.enemies.Herald import Herald
from gameMap.MapPosition import MapPosition
from items.equipables.weapons.EdgeOfChaos import EdgeOfChaos


class HeraldOfChaos(Herald):

    def __init__(self, game_panel, position: MapPosition):
        super().__init__(game_panel, position)

        self.set_name("Herald of chaos")

        self.set_max_hitpoints(160)
        self.set_hitpoints(self.get_max_hitpoints())
        self.set_thrust_defence(2)
        self.set_swing_defence(2)
        self.set_magic_defence(2)

        self.set_main_hand(EdgeOfChaos(self.get_position()))

        self.set_experience_points(400)

    def init_appearance_on_level(self):
        return [6]