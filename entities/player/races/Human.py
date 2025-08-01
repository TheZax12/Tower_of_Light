from entities.player.races.Race import Race
from entities.player.Player import Player


class Human(Race):

    def init_stats(self, player: Player):
        player.set_strength(9)
        player.set_intellect(9)
        player.set_swing_defence(1)
        player.set_thrust_defence(1)
        player.set_magic_defence(1)

    def init_race(self):
        self.set_race("Human")