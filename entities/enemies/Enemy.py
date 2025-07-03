from entities.Entity import Entity

from UI.Colors import *


class Enemy(Entity):

    def __init__(self, position):
        super().__init__(position)
        self.discovered = False
        self.visible = False

    def set_name(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name
    
    def apperance_on_level(self):        
        from entities.enemies import Priest, Vampire, Knight, ChaosKnight, Bishop, Summoner, Paladin, FallenHero, Archangel, Fiend, HeraldOfLight, HeraldOfChaos

        if isinstance(self, (Priest.Priest, Vampire.Vampire)):
            level_apperance = [1, 2]
        elif isinstance(self, (Knight.Knight, ChaosKnight.ChaosKnight, Bishop.Bishop, Summoner.Summoner)):
            level_apperance = [2, 3, 4]
        elif isinstance(self, (Paladin.Paladin, FallenHero.FallenHero)):
            level_apperance = [3, 4, 5]
        elif isinstance(self, Archangel.Archangel):
            level_apperance = [4, 5, 6]
        elif isinstance(self, Fiend.Fiend):
            level_apperance = [5, 6]
        elif isinstance(self, (HeraldOfLight.HeraldOfLight, HeraldOfChaos.HeraldOfChaos)):
            level_apperance = [6]
        else:
            level_apperance = []
        return level_apperance
    
    def set_discovered(self, discovered: bool):
        self.discovered = discovered

    def is_discovered(self) -> bool:
        return self.discovered
    
    def set_visible(self, visible: bool):
        self.visible = visible
    
    def is_visible(self) -> bool:
        return self.visible
    
    def set_visible_color(self, color):
        self.visible_color = color

    def set_invisible_color(self, color):
        self.invisible_color = color