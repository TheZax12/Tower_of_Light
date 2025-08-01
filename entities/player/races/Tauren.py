from entities.player.races.Race import Race
from entities.player.Player import Player


class Tauren(Race):

    def init_stats(self, player: Player):
        player.set_strength(12)
        player.set_intellect(6)
        player.set_swing_defence(1)
        player.set_thrust_defence(2)
        player.set_magic_defence(0)

    def init_race(self):
        self.set_race("Tauren")