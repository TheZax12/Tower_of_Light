import pygame
import math

from log.LogSubject import LogSubject
from entities.Direction import Direction
from gameMap.MapPosition import MapPosition
from items.equipables.weapons.Weapon import Weapon
from items.equipables.Damage import DamageType

from gameMap.MapSettings import tile_size


class Entity:
    
    def __init__(self, game_panel, position: MapPosition):
        self.game_panel = game_panel
        self.position = position
        self.direction = Direction.NONE
        self.collision = False

        self.set_rect(pygame.Rect(self.get_position().get_tile_x(), self.get_position().get_tile_y(), tile_size, tile_size))
        
    def set_position(self, position: MapPosition):
        self.position = position

    def get_position(self) -> MapPosition:
        return self.position
    
    def set_direction(self, direction: Direction):
        self.direction = direction

    def get_direction(self) -> Direction:
        return self.direction
    
    def set_collision(self, collision: bool):
        self.collision = collision

    def get_collision(self) -> bool:
        return self.collision
    
    def set_rect(self, rect: pygame.Rect):
        self.rect = rect
    
    def get_rect(self) -> pygame.Rect:
        return self.rect
    
    def update_rect(self):
        self.get_rect().topleft = (self.get_position().get_tile_x(), self.get_position().get_tile_y())

    def set_hitpoints(self, hitpoints: int):
        self.hitpoints = hitpoints

    def get_hitpoints(self) -> int:
        return self.hitpoints
    
    def set_max_hitpoints(self, max_hitpoints: int):
        self.max_hitpoints = max_hitpoints

    def get_max_hitpoints(self) -> int:
        return self.max_hitpoints
    
    def set_swing_defence(self, swing_defence: int):
        self.swing_defence = swing_defence

    def get_swing_defence(self) -> int:
        return self.swing_defence
    
    def set_thrust_defence(self, thrust_defence: int):
        self.thrust_defence = thrust_defence

    def get_thrust_defence(self) -> int:
        return self.thrust_defence
    
    def set_magic_defence(self, magic_defence: int):
        self.magic_defence = magic_defence
    
    def get_magic_defence(self) -> int:
        return self.magic_defence
    
    def set_experience_points(self, experience_points: int):
        self.experience_points = experience_points

    def get_experience_points(self) -> int:
        return self.experience_points

    def set_main_hand(self, main_hand: Weapon):
        self.main_hand = main_hand

    def get_main_hand(self) -> Weapon:
        return self.main_hand
    
    def move_up(self):
        self.set_position(self.get_position().above())

    def move_down(self):
        self.set_position(self.get_position().below())

    def move_left(self):
        self.set_position(self.get_position().left())

    def move_right(self):
        self.set_position(self.get_position().right())

    def set_direction_before_moving(self):
        pass

    def check_for_wall_collision(self, entity_rect: pygame.Rect) -> bool:
        """ Checks for entity-wall collision. """
        for wall_tile in self.game_panel.tile_manager.get_wall_tiles():
            if entity_rect.colliderect(wall_tile.get_rect()):
                return True
        return False

    def allowed_position(self):
        pass

    def move(self):
        if not self.get_collision():
            match self.get_direction():
                case Direction.UP:
                    self.move_up()
                case Direction.DOWN:
                    self.move_down()
                case Direction.LEFT:
                    self.move_left()
                case Direction.RIGHT:
                    self.move_right()
            self.update_rect()

    def damage_amount_received(self, damage_amount: int, defence_amount_getter, damage_type: DamageType):
        log_subject = LogSubject()
        
        defence_amount = defence_amount_getter()
        if defence_amount == math.inf:
            log_subject.notify_log_observer(f"{self.__class__.__name__.capitalize()} immune to {damage_type.name.lower()} damage.")
            return
        
        damage_dealt = damage_amount - defence_amount
        if damage_dealt <= 0:
            return
        
        if self.get_hitpoints() <= damage_dealt:
            self.set_hitpoints(0)
            return
        
        self.set_hitpoints(self.get_hitpoints() - damage_dealt)

    def damage_type_received(self, damage_type: DamageType, damage_amount: int):
        if damage_type == DamageType.THRUST:
            self.damage_amount_received(damage_amount, self.get_thrust_defence, damage_type)
        elif damage_type == DamageType.SWING:
            self.damage_amount_received(damage_amount, self.get_swing_defence, damage_type)
        elif damage_type == DamageType.MAGIC:
            self.damage_amount_received(damage_amount, self.get_magic_defence, damage_type)

    def attack_received(self, damage_list):
        for damage in damage_list:
            self.damage_type_received(damage.get_damage_type(), damage.get_damage_amount())

        if self.get_hitpoints() <= 0:
            self.die()
    
    def attack(self, damage_list, target):
        target.attack_received(damage_list)

    def die(self):
        pass