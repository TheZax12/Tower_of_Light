class Warrior:
    
    def __init__(self):
        self.init_warrior()
    
    def set_warrior(self, warrior: str):
        self.warrior = warrior

    def get_warrior(self) -> str:
        return self.warrior
    
    def init_warrior(self):
        pass

    def update_stats(self, player):
        pass

    @staticmethod
    def warriors(warrior: str):
        from entities.player.races.warriors.Knight import Knight
        from entities.player.races.warriors.Paladin import Paladin
        from entities.player.races.warriors.Mage import Mage
        
        match warrior:
            case "Knight": return Knight()
            case "Paladin": return Paladin()
            case "Mage": return Mage()
            case _: 
                raise ValueError(f"Unknown warrior: {warrior}")