from entities.enemies.Enemy import Enemy


class Herald(Enemy):

    def __init__(self, game_panel, position):
        super().__init__(game_panel, position)

    def damage_amount_received(self, damage_amount: int, defence_amount_getter, damage_type):        
        defence_amount = defence_amount_getter()
        
        damage_dealt = round(damage_amount / defence_amount)

        if damage_dealt <= 0:
            return
        
        if self.get_hitpoints() <= damage_dealt:
            self.set_hitpoints(0)
            return
        
        self.set_hitpoints(self.get_hitpoints() - damage_dealt)
