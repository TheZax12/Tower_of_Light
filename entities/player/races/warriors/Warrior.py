class Warrior:
    
    def __init__(self):
        self.init_warrior()
    
    def set_warrior(self, warrior: str):
        self.warrior = warrior

    def get_warrior(self) -> str:
        return self.warrior
    
    def init_warrior(self):
        pass

    def update_stats(self):
        pass

    def init_starter_weapon(self):
        pass

    @staticmethod
    def warriors(warrior: str):        
        match warrior:
            case "Knight":
                from entities.player.races.warriors.Knight import Knight
                return Knight()
            case "Paladin":
                from entities.player.races.warriors.Paladin import Paladin
                return Paladin()
            case "Mage":
                from entities.player.races.warriors.Mage import Mage                
                return Mage()
            case _: 
                raise ValueError(f"Unknown warrior: {warrior}")