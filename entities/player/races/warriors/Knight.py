from entities.player.Player import Player
from entities.player.races.warriors.Warrior import Warrior
from items.equipables.weapons.WoodenSword import WoodenSword


class Knight(Warrior):

    def update_stats(self, player: Player):
        match player.get_level():
            case 1:
                player.set_max_hitpoints(player.get_max_hitpoints() + 10)
                player.set_strength(player.get_strength() + 2)
            case 2:
                player.set_max_hitpoints(player.get_max_hitpoints() + 15)
                player.set_strength(player.get_strength() + 4)
            case 3:
                player.set_max_hitpoints(player.get_max_hitpoints() + 20)
                player.set_strength(player.get_strength() + 6)
            case 4:
                player.set_max_hitpoints(player.get_max_hitpoints() + 25)
                player.set_strength(player.get_strength() + 8)
            case 5:
                player.set_max_hitpoints(player.get_max_hitpoints() + 30)
                player.set_strength(player.get_strength() + 10)
            case 6:
                player.set_max_hitpoints(player.get_max_hitpoints() + 40)
                player.set_strength(player.get_strength() + 12)

    def init_warrior(self):
        self.set_warrior("Knight")

    def set_starter_weapon(self, player: Player):
        player.set_main_hand(WoodenSword(player.get_position()))

    def set_secondary_weapon(self, player: Player):
        player.set_off_hand(None)