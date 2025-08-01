import pygame
import random

from log.LogSubject import LogSubject
from entities.Entity import Entity
from entities.Direction import Direction
from entities.enemies.PathFinder import PathFinder
from gameMap.tiles.TileType import TileType
from items.usables.HealthPotion import HealthPotion
from items.usables.ManaPotion import ManaPotion
from gameMap.MapPosition import MapPosition

from gameMap.MapSettings import map_width, map_height, tile_size
from UI.Colors import *


class Enemy(Entity):

    def __init__(self, game_panel, position: MapPosition):
        super().__init__(game_panel, position)
        self.discovered = False
        self.visible = False

        self.visibility_radius = 8
        self.level_appearance = self.init_appearance_on_level()

    def set_name(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name
    
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

    def init_appearance_on_level(self):
        pass

    def get_appearance_on_level(self):
        return self.level_appearance
    
    def generate_random_position(self):
        tile_manager = self.game_panel.tile_manager
        player = self.game_panel.player
        
        while True:
            random_x = random.randint(0, map_width - 1)
            random_y = random.randint(0, map_height - 1)
            random_position = MapPosition.generate_position(random_x, random_y)

            if (not tile_manager.get_tile(random_position).get_type() == TileType.WALL and
               random_position.distance_to(player.get_position()) > player.visibility_radius):
                self.set_position(random_position)
                break

    def increase_hitpoints_on_beacon_creation(self, increase_factor: int):
        increased_max_hp = int(round(increase_factor * self.get_max_hitpoints()))
        self.set_max_hitpoints(increased_max_hp)

        increased_hp = int(round(increase_factor * self.get_hitpoints()))
        if increased_hp > increased_max_hp:
            self.set_hitpoints(self.get_max_hitpoints())
        else:
            self.set_hitpoints(increased_hp)

    def increase_damage_on_beacon_creation(self, increase_factor: int):
        for damage in self.get_main_hand().get_damage_list():
            increased_damage = int(round(increase_factor * damage.get_damage_amount()))
            damage.enhance(increased_damage)

    def increase_experience_points_on_beacon_creation(self, increase_factor: int):
        increased_xp = int(round(increase_factor * self.get_experience_points()))
        self.set_experience_points(increased_xp)

    def buff_on_beacon_creation(self):
        increase_factor = 1.25
        self.increase_hitpoints_on_beacon_creation(increase_factor)
        self.increase_damage_on_beacon_creation(increase_factor)
        self.increase_experience_points_on_beacon_creation(increase_factor)
    
    def set_direction_before_moving(self, next_position: MapPosition):
        """Sets the direction of the enemy before moving."""
        if next_position.get_tile_x() < self.get_position().get_tile_x():
            self.set_direction(Direction.LEFT)
        elif next_position.get_tile_x() > self.get_position().get_tile_x():
            self.set_direction(Direction.RIGHT)
        elif next_position.get_tile_y() < self.get_position().get_tile_y():
            self.set_direction(Direction.UP)
        elif next_position.get_tile_y() > self.get_position().get_tile_y():
            self.set_direction(Direction.DOWN)
        else:
            self.set_direction(Direction.NONE)

    def check_for_player_collision(self, enemy_rect):
        """Checks for enemy-player collision."""
        player = self.game_panel.player
        if enemy_rect.colliderect(player.get_rect()):
            return True
        return False

    def allowed_position(self, next_position):
        temp_rect = pygame.Rect(next_position.get_tile_x(), next_position.get_tile_y(), tile_size, tile_size)
        collided = self.check_for_player_collision(temp_rect)
        self.set_collision(collided)

    def move(self):
        player = self.game_panel.player
        tile_manager = self.game_panel.tile_manager
        
        pathfinder = PathFinder(tile_manager)
        distance_to_player = self.get_position().distance_to(player.get_position())
        if distance_to_player <= self.visibility_radius:
            path = pathfinder.find_path(self.get_position(), player.get_position())
            
            if len(path) > 1:
                next_position = path[1]
                self.allowed_position(next_position)
                self.set_direction_before_moving(next_position)
                super().move()

    def die(self):
        enemy_manager = self.game_panel.enemy_manager
        item_manager = self.game_panel.item_manager
        player = self.game_panel.player
        
        # Notify log observer about the enemy's death.
        log_subject = LogSubject()
        log_subject.notify_log_observer(f"{self.get_name()} has been defeated.")

        # Remove the enemy from the game.
        enemy_manager.bury_enemy(self)

        # Drop enemy's weapon.
        enemy_weapon = self.get_main_hand()
        enemy_weapon.set_position(self.get_position())
        item_manager.create_item(enemy_weapon)

        # Drop random usable item.
        usable_item_drop_chance = 0.7
        if random.random() < usable_item_drop_chance:
            usable_items_list = [HealthPotion(self.get_position()), ManaPotion(self.get_position())]
            random_usable_item = random.choice(usable_items_list)
            item_manager.create_item(random_usable_item)

        # Give experience points to the player.
        player.set_experience_points(player.get_experience_points() + self.get_experience_points())
    
    def attack(self, opportunity_attack=False):
        log_subject = LogSubject()
        player = self.game_panel.player
        
        attack_distance = 1
        if opportunity_attack or self.get_position().distance_to(player.get_position()) == attack_distance:
            super().attack(self.get_main_hand().get_damage_list(), player)
            log_subject.notify_log_observer(f"Attacked by {self.get_name()}.")

    def visibility(self):
        player = self.game_panel.player
        distance_to_player = self.get_position().distance_to(player.get_position())
        if distance_to_player <= player.visibility_radius:
            self.set_visible(True)
            if not self.is_discovered():
                self.set_discovered(True)
        else:
            self.set_visible(False)

    def update(self, allow_attack=True):
        self.visibility()
        self.move()
        if allow_attack:
            self.attack()

    def draw_visible(self, display_surface: pygame.Surface):
        pygame.draw.rect(display_surface, enemy_visible_color, self.get_rect())

    def draw_invisible(self, display_surface: pygame.Surface):
        tile_manager = self.game_panel.tile_manager
        # Light is restrored to the level
        if len(tile_manager.beacon_tiles) == tile_manager.max_beacon_number:
            pygame.draw.rect(display_surface, enemy_invinsible_color, self.get_rect())
        # Level in chaos
        else:
            enemy_tile = tile_manager.get_tile(self.get_position())
            enemy_tile.draw_tile(display_surface)

    def draw(self, display_surface: pygame.Surface):
        # Draw the enemy.
        if self.is_visible():
            self.draw_visible(display_surface)
        else:
            self.draw_invisible(display_surface)

        # Draw the rectangle's border.
        pygame.draw.rect(display_surface, (0, 0, 0), self.get_rect(), 1)