import pygame
import random

from entities.enemies import Archangel, Bishop, ChaosKnight, FallenHero, Fiend, HeraldOfChaos, HeraldOfLight, Knight, Paladin, Priest, Summoner, Vampire
from log.LogSubject import LogSubject

from gameMap.MapSettings import tile_size, default_position
from UI.Colors import *


class EnemyManager:

    def __init__(self, game_panel):
        self.game_panel = game_panel
        self.log_subject = LogSubject()

        self.enemies_starting_number = 3
        self.all_enemies_types = [Archangel.Archangel,
                                 Bishop.Bishop,
                                 ChaosKnight.ChaosKnight,
                                 FallenHero.FallenHero,
                                 Fiend.Fiend,
                                 HeraldOfChaos.HeraldOfChaos,
                                 HeraldOfLight.HeraldOfLight,
                                 Knight.Knight,
                                 Paladin.Paladin,
                                 Priest.Priest,
                                 Summoner.Summoner,
                                 Vampire.Vampire]
        self.generated_enemies_list = []

        self.reset()

    def get_generated_enemies(self):
        return self.generated_enemies_list
    
    def get_close_up_enemies(self, close_distance: int):
        player = self.game_panel.player
        close_up_enemies_list = []
        for enemy in self.generated_enemies_list:
            if enemy.get_position().distance_to(player.get_position()) <= close_distance:
                close_up_enemies_list.append(enemy)
        return close_up_enemies_list
    
    def bury_enemy(self, enemy):
        self.generated_enemies_list.remove(enemy)
        
    def generate_random_enemy(self):
        while True:
            random_enemy_class = random.choice(self.all_enemies_types)
            random_enemy = random_enemy_class(self.game_panel, default_position)
            if self.game_panel.get_game_level() in random_enemy.get_appearance_on_level():
                random_enemy.generate_random_position()
                self.generated_enemies_list.append(random_enemy)
                random_enemy.set_rect(pygame.Rect(random_enemy.get_position().get_tile_x(), random_enemy.get_position().get_tile_y(), tile_size, tile_size))
                return

    def increase_enemies_on_beacon_creation(self):
        increase_factor = 2
        for _ in range(increase_factor):
            self.generate_random_enemy()
        self.log_subject.notify_log_observer("Two more enemies have been spawned.")

    def buff_enemies_on_beacon_creation(self):
        for enemy in self.generated_enemies_list:
            enemy.buff_on_beacon_creation()

    def update_on_beacon_creation(self):
        self.increase_enemies_on_beacon_creation()
        self.buff_enemies_on_beacon_creation()

    def update(self):
        close_distance = 1
        adjacent_enemies = self.get_close_up_enemies(close_distance)

        # In case of multiple asjacent enemies, only the strongest one attacks.
        strongest_adjacent_enemy = None
        if adjacent_enemies:
            strongest_adjacent_enemy = max(
                adjacent_enemies,
                key=lambda enemy: (enemy.get_max_hitpoints(), enemy.get_experience_points())
            )

        for enemy in self.generated_enemies_list:
            if enemy is strongest_adjacent_enemy:
                enemy.update(allow_attack=True)
            else:
                enemy.update(allow_attack=False)

    def reset(self):
        self.generated_enemies_list.clear()
        for _ in range(self.enemies_starting_number):
            self.generate_random_enemy()

    def draw_enemies(self, display_surface: pygame.Surface):
        for enemy in self.generated_enemies_list:
            enemy.draw(display_surface)