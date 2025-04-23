class Race:

    def __init__(self):
        self.init_race()

    def set_race(self, race: str):
        self.race = race

    def get_race(self) -> str:
        return self.race
    
    def init_race(self):
        pass
    
    def init_stats(self, player):
        pass

    @staticmethod
    def races(race: str):
        from entities.player.races.Human import Human
        from entities.player.races.Elf import Elf
        from entities.player.races.Orc import Orc
        from entities.player.races.Tauren import Tauren
        
        match race:
            case "Human": return Human()
            case "Elf": return Elf()
            case "Orc": return Orc()
            case "Tauren": return Tauren()
            case _: 
                raise ValueError(f"Unknown race: {race}")