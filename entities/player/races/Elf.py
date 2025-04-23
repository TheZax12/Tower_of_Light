from entities.player.races.Race import Race
from entities.player.Player import Player


class Elf(Race):

    def init_stats(self, player: Player):
        player.set_strength(6)
        player.set_intelect(12)
        player.set_swing_defence(0)
        player.set_thrust_defence(1)
        player.set_magic_defence(2)

    def init_race(self):
        self.set_race("Elf")