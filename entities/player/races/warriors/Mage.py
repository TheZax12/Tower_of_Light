from entities.player.Player import Player
from entities.player.races.warriors.Warrior import Warrior


class Mage(Warrior):

    def update_stats(self, player: Player):
        match player.get_level():
            case 1:
                player.set_max_hitpoints(player.get_max_hitpoints() + 8)
                player.set_max_manapoints(player.get_max_manapoints() + 12)
                player.set_strength(player.get_strength() + 2)
                player.set_intelect(player.get_intellect() + 8)
            case 2:
                player.set_max_hitpoints(player.get_max_hitpoints() + 12)
                player.set_max_manapoints(player.get_max_manapoints() + 40)
                player.set_strength(player.get_strength() + 3)
                player.set_intelect(player.get_intellect() + 16)
            case 3:
                player.set_max_hitpoints(player.get_max_hitpoints() + 16)
                player.set_max_manapoints(player.get_max_manapoints() + 60)
                player.set_strength(player.get_strength() + 4)
                player.set_intelect(player.get_intellect() + 24)
            case 4:
                player.set_max_hitpoints(player.get_max_hitpoints() + 20)
                player.set_max_manapoints(player.get_max_manapoints() + 80)
                player.set_strength(player.get_strength() + 5)
                player.set_intelect(player.get_intellect() + 32)
            case 5:
                player.set_max_hitpoints(player.get_max_hitpoints() + 24)
                player.set_max_manapoints(player.get_max_manapoints() + 100)
                player.set_strength(player.get_strength() + 6)
                player.set_intelect(player.get_intellect() + 40)
            case 6:
                player.set_max_hitpoints(player.get_max_hitpoints() + 30)
                player.set_max_manapoints(player.get_max_manapoints() + 120)
                player.set_strength(player.get_strength() + 7)
                player.set_intelect(player.get_intellect() + 48)

    def init_warrior(self):
        self.set_warrior("Mage")