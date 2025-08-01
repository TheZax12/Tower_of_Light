from entities.player.Player import Player
from entities.player.races.warriors.Warrior import Warrior
from items.equipables.weapons.Spear import Spear


class Paladin(Warrior):

    def update_stats(self, player: Player):
        match player.get_level():
            case 1:
                player.set_max_hitpoints(player.get_max_hitpoints() + 10)
                player.set_max_manapoints(player.get_max_manapoints() + 10)
                player.set_strength(player.get_strength() + 5)
                player.set_intellect(player.get_intellect() + 5)
            case 2:
                player.set_max_hitpoints(player.get_max_hitpoints() + 13)
                player.set_max_manapoints(player.get_max_manapoints() + 20)
                player.set_strength(player.get_strength() + 7)
                player.set_intellect(player.get_intellect() + 9)
            case 3:
                player.set_max_hitpoints(player.get_max_hitpoints() + 16)
                player.set_max_manapoints(player.get_max_manapoints() + 30)
                player.set_strength(player.get_strength() + 9)
                player.set_intellect(player.get_intellect() + 13)
            case 4:
                player.set_max_hitpoints(player.get_max_hitpoints() + 20)
                player.set_max_manapoints(player.get_max_manapoints() + 40)
                player.set_strength(player.get_strength() + 11)
                player.set_intellect(player.get_intellect() + 17)
            case 5:
                player.set_max_hitpoints(player.get_max_hitpoints() + 28)
                player.set_max_manapoints(player.get_max_manapoints() + 50)
                player.set_strength(player.get_strength() + 13)
                player.set_intellect(player.get_intellect() + 21)
            case 6:
                player.set_max_hitpoints(player.get_max_hitpoints() + 40)
                player.set_max_manapoints(player.get_max_manapoints() + 70)
                player.set_strength(player.get_strength() + 15)
                player.set_intellect(player.get_intellect() + 25)

    def init_warrior(self):
        self.set_warrior("Paladin")

    def set_starter_weapon(self, player: Player):
        player.set_main_hand(Spear(player.get_position()))

    def set_secondary_weapon(self, player: Player):
        player.set_off_hand(None)