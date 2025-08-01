import pygame

from entities.Entity import Entity
from entities.player.races.Race import Race
from entities.player.races.warriors.Warrior import Warrior
from entities.Direction import Direction
from items.usables.HealthPotion import HealthPotion
from items.usables.ManaPotion import ManaPotion
from items.equipables.EquipableItem import EquipableItem
from items.ItemEffect import ItemEffect
from items.ItemEffect import ItemEffectType
from items.equipables.Damage import Damage, DamageType
from items.equipables.Dice import Dice
from gameMap.MapPosition import MapPosition
from log.LogSubject import LogSubject

from gameMap.MapSettings import *
from UI.Colors import player_color


class Player(Entity):
    
    def __init__(self, game_panel, position: MapPosition, race: Race, warrior: Warrior):
        self.log_subject = LogSubject()
        
        super().__init__(game_panel, position)
        self.visibility_radius = 6
        
        self.race = race
        self.warrior = warrior

        self.name = self.race.get_race() + " " + self.warrior.get_warrior()

        self.beacon_casting_cooldown = 20
        self.resting_cooldown = 7

        self.restart()
        
    def get_name(self) -> str:
        return self.name
    
    def set_level(self, level: int):
        self.level = level

    def get_level(self) -> int:
        return self.level
    
    def set_manapoints(self, manapoints: int):
        self.manapoints = manapoints

    def get_manapoints(self) -> int:
        return self.manapoints
    
    def set_max_manapoints(self, max_manapoints: int):
        self.max_manapoints = max_manapoints

    def get_max_manapoints(self) -> int:
        return self.max_manapoints
    
    def set_strength(self, strength: int):
        self.strength = strength

    def get_strength(self) -> int:
        return self.strength
    
    def set_intellect(self, intellect: int):
        self.intellect = intellect

    def get_intellect(self) -> int:
        return self.intellect
    
    def set_off_hand(self, off_hand: EquipableItem):
        self.off_hand = off_hand

    def get_off_hand(self) -> EquipableItem:
        return self.off_hand
    
    def set_actions_number(self, actions_number: int):
        self.actions_number = actions_number

    def get_actions_number(self) -> int:
        return self.actions_number
    
    def set_take_turn(self, take_turn: bool):
        self.take_turn = take_turn

    def get_take_turn(self) -> bool:
        return self.take_turn
    
    def set_item_selection(self, item_selection: bool):
        self.item_selection = item_selection

    def get_item_selection(self) -> bool:
        return self.item_selection
    
    def update_level(self):
        xp = self.get_experience_points()

        if xp < 300:
            level = 1
        elif xp < 900:
            level = 2
        elif xp < 2700:
            level = 3
        elif xp < 6500:
            level = 4
        elif xp < 14000:
            level = 5
        else:
            level = 6

        if level != self.get_level():
            self.set_level(level)
            self.log_subject.notify_log_observer(f"Player leveled up.")
            self.warrior.update_stats(self)
            self.log_subject.notify_log_observer(f"Player stats updated.")

    def get_xp_to_level_up(self):
        if self.get_level() == 1:
            return 300
        elif self.get_level() == 2:
            return 900
        elif self.get_level() == 3:
            return 2700
        elif self.get_level() == 4:
            return 6500
        elif self.get_level() == 5:
            return 14000
        elif self.get_level() == 6:
            return None
    
    def player_stats(self):
        current_xp = self.get_experience_points()
        xp_to_level_up = self.get_xp_to_level_up()
        if xp_to_level_up is None:
            xp_message = "max level"
        else:
            xp_message = f"{current_xp}/{xp_to_level_up} xp"
        
        return (
            f"Name: {self.get_name()}\n"
            f"Level: {self.get_level()} ({xp_message})\n"
            f"Hitpoints: {self.get_hitpoints()}/{self.get_max_hitpoints()}\n"
            f"Manapoints: {self.get_manapoints()}/{self.get_max_manapoints()}\n"
            f"Strength: {self.get_strength()}\n"
            f"Intellect: {self.get_intellect()}\n"
            f"Swing Defence: {self.get_swing_defence()}\n"
            f"Thrust Defence: {self.get_thrust_defence()}\n"
            f"Magic Defence: {self.get_magic_defence()}\n"
        )

    def create_beacon(self):
        tile_manager = self.game_panel.tile_manager

        if len(tile_manager.beacon_tiles) < tile_manager.max_beacon_number:
                if tile_manager.beacons_min_distance(self.get_position()) < tile_manager.min_beacon_distance:
                    self.log_subject.notify_log_observer("Cannot place a beacon here. It's too close to another beacon.")
                    return
                elif tile_manager.min_player_spawn_beacon_distance(self.get_position()) < tile_manager.min_beacon_distance:
                    self.log_subject.notify_log_observer("Cannot place a beacon here. It's too close to the player spawn.")
                    return
                elif self.get_position() == exit_spawn:
                    self.log_subject.notify_log_observer("Cannot place a beacon on the exit tile.")
                    return
                elif self.get_actions_number() - self.last_beacon_cast_action < self.beacon_casting_cooldown:
                    actions_left = self.beacon_casting_cooldown - (self.get_actions_number() - self.last_beacon_cast_action)
                    self.log_subject.notify_log_observer(f"Beacon casting cooldown: {actions_left} actions remaining.")
                else:
                    tile_manager.add_beacon(self.get_position())
                    self.last_beacon_cast_action = self.get_actions_number()
                    self.set_experience_points(self.get_experience_points() + 100)
                    self.set_actions_number(self.get_actions_number() + 1)
                    self.set_take_turn(True)
        else:
            self.log_subject.notify_log_observer("Maximum number of beacons reached.")
    
    def item_effect_on_player(self, item_effect: ItemEffect):
        match item_effect.effect_type:
            case ItemEffectType.HP_REPLENISHMENT:
                updated_stat = self.get_hitpoints() + item_effect.stat_enhancement
                self.set_hitpoints(min(updated_stat, self.get_max_hitpoints()))
            case ItemEffectType.MP_REPLENISHMENT:
                updated_stat = self.get_manapoints() + item_effect.stat_enhancement
                self.set_manapoints(min(updated_stat, self.get_max_manapoints()))
            case ItemEffectType.HP_BOOST:
                self.set_max_hitpoints(self.get_max_hitpoints() + item_effect.stat_enhancement)
            case ItemEffectType.MP_BOOST:
                self.set_max_manapoints(self.get_max_manapoints() + item_effect.stat_enhancement)
            case ItemEffectType.STR_BOOST:
                self.set_strength(self.get_strength() + item_effect.stat_enhancement)
            case ItemEffectType.INT_BOOST:
                self.set_intellect(self.get_intellect() + item_effect.stat_enhancement)

    def consume_usable_item(self, usable_item):        
        for item_effect in usable_item.use():
            self.item_effect_on_player(item_effect)
        self.game_panel.inventory.remove_used_items()
        self.set_actions_number(self.get_actions_number() + 1)
        self.set_take_turn(True)

    def consume_healing_potion(self):
        healing_potion = self.game_panel.inventory.get_item_type(HealthPotion)
        
        if not healing_potion:
            self.log_subject.notify_log_observer("No healing potions in inventory.")
            return
        
        if self.get_hitpoints() == self.get_max_hitpoints():
            self.log_subject.notify_log_observer("Cannot use healing potion, hitpoints are already full.")
            return
        
        self.consume_usable_item(healing_potion[0])

    def consume_mana_potion(self):
        mana_potion = self.game_panel.inventory.get_item_type(ManaPotion)

        if not mana_potion:
            self.log_subject.notify_log_observer("No mana potions in inventory.")
            return
        
        if self.get_manapoints() == self.get_max_manapoints():
            self.log_subject.notify_log_observer("Cannot use mana potion, manapoints are already full.")
            return
        
        self.consume_usable_item(mana_potion[0])

    def apply_equipable_item_effects(self, equipable_item: EquipableItem):
        for item_effect in equipable_item.get_item_effects():
            self.item_effect_on_player(item_effect)

        if self.get_hitpoints() > self.get_max_hitpoints():
            self.set_hitpoints(self.get_max_hitpoints())

        if self.get_manapoints() > self.get_max_manapoints():
            self.set_manapoints(self.get_max_manapoints())

    def undo_equipable_item_effects(self, equipable_item: EquipableItem):
        for item_effect in equipable_item.get_unequip_item_effects():
            self.item_effect_on_player(item_effect)

    def change_equipable_item(self, event, equipped_item: EquipableItem, equipable_item_setter):
        item_manager = self.game_panel.item_manager
        equipable_items_on_tile = item_manager.equipable_items.get(self.get_position(), [])

        if not equipable_items_on_tile:
            self.log_subject.notify_log_observer("No item to equip on this tile.")
            self.set_item_selection(False)
            return

        if len(equipable_items_on_tile) == 1:
            chosen_item = equipable_items_on_tile[0]
        else:
            if not self.get_item_selection():
                self.set_item_selection(True)
                self.log_subject.notify_log_observer("Press the corresponding number to select an item...")
                self.pending_equip_setter = equipable_item_setter
                return

            if pygame.K_1 <= event.key <= pygame.K_9:
                index = event.key - pygame.K_1  # 0-based index
            elif pygame.K_KP1 <= event.key <= pygame.K_KP9:
                index = event.key - pygame.K_KP1  # 0-based index
            else:
                self.log_subject.notify_log_observer("Invalid key. Item selection cancelled.")
                self.set_item_selection(False)
                return

            if 0 <= index < len(equipable_items_on_tile):
                chosen_item = equipable_items_on_tile[index]
            else:
                self.log_subject.notify_log_observer("Invalid item number.")
                self.set_item_selection(False)
                return

        # Drop currently equipped item
        if equipped_item is not None:
            equipped_item.set_position(self.get_position())
            self.undo_equipable_item_effects(equipped_item)
            item_manager.create_item(equipped_item)
            self.log_subject.notify_log_observer(f"Dropped {equipped_item.get_item_name().lower()}.")

        # Remove the chosen item from the tile
        equipable_items_on_tile.remove(chosen_item)
        if not equipable_items_on_tile:
            del item_manager.equipable_items[self.get_position()]

        # Equip the chosen item
        equipable_item_setter(chosen_item)
        self.apply_equipable_item_effects(chosen_item)
        self.set_item_selection(False)
        self.log_subject.notify_log_observer(f"Equipped {chosen_item.get_item_name().lower()}.")

    def change_main_weapon(self, event):
        self.change_equipable_item(event, self.get_main_hand(), self.set_main_hand)

    def change_secondary_weapon(self, event):
        self.change_equipable_item(event, self.get_off_hand(), self.set_off_hand)

    def swap_weapons(self):
        main_weapon = self.get_main_hand()
        secondary_weapon = self.get_off_hand()

        if secondary_weapon is None:
            return
        
        # Undo the effects
        self.undo_equipable_item_effects(main_weapon)
        self.undo_equipable_item_effects(secondary_weapon)

        # Swap the weapons
        self.set_main_hand(secondary_weapon)
        self.set_off_hand(main_weapon)

        # Reapply the effects
        self.apply_equipable_item_effects(self.get_main_hand())
        self.apply_equipable_item_effects(self.get_off_hand())

        self.log_subject.notify_log_observer("Swapped weapons.")

    def stat_replenish(self, current_stat, max_stat, replenish_factor):
        replenish = round(max_stat * replenish_factor)
        if replenish == 0:
            replenish = 1
        
        replenished_stat = current_stat + replenish
        return replenished_stat

    def execute_rest(self):
            if self.get_actions_number() - self.last_rest_action < self.resting_cooldown:
                actions_left = self.resting_cooldown - (self.get_actions_number() - self.last_rest_action)
                self.log_subject.notify_log_observer(f"Resting cooldown: {actions_left} actions remaining.")
                return

            if self.get_hitpoints() < self.get_max_hitpoints() or self.get_manapoints() < self.get_max_manapoints():
                self.log_subject.notify_log_observer("Resting...")
                if self.get_hitpoints() < self.get_max_hitpoints() and self.get_manapoints() < self.get_max_manapoints():
                    hitpoints_replenished = self.stat_replenish(self.get_hitpoints(), self.get_max_hitpoints(), 0.05)
                    manapoints_replenished = self.stat_replenish(self.get_manapoints(), self.get_max_manapoints(), 0.05)
                    self.log_subject.notify_log_observer(f"Gained {hitpoints_replenished - self.get_hitpoints()} health points and {manapoints_replenished - self.get_manapoints()} mana points.")
                    self.set_hitpoints(min(hitpoints_replenished, self.get_max_hitpoints()))
                    self.set_manapoints(min(manapoints_replenished, self.get_max_manapoints()))
                elif self.get_hitpoints() < self.get_max_hitpoints():
                    hitpoints_replenished = self.stat_replenish(self.get_hitpoints(), self.get_max_hitpoints(), 0.05)
                    self.log_subject.notify_log_observer(f"Gained {hitpoints_replenished - self.get_hitpoints()} health points.")
                    self.set_hitpoints(min(hitpoints_replenished, self.get_max_hitpoints()))
                elif self.get_manapoints() < self.get_max_manapoints():
                    manapoints_replenished = self.stat_replenish(self.get_manapoints(), self.get_max_manapoints(), 0.05)
                    self.log_subject.notify_log_observer(f"Gained {manapoints_replenished - self.get_manapoints()} mana points.")
                    self.set_manapoints(min(manapoints_replenished, self.get_max_manapoints()))
                self.last_rest_action = self.get_actions_number()
                self.set_actions_number(self.get_actions_number() + 1)
                self.set_take_turn(True)
            else:
                self.log_subject.notify_log_observer("Resting has no effect. Hitpoints and manapoints are already full.")
    
    def base_attack_damage_calculation(self):        
        damage_list = self.get_main_hand().get_damage_list()
        for damage in damage_list:
            if damage.get_damage_type() == DamageType.SWING or damage.get_damage_type() == DamageType.THRUST:
                damage.enhance(self.get_strength())
            elif damage.get_damage_type() == DamageType.MAGIC:
                damage.enhance(self.get_intellect())
        return damage_list
    
    def spell_attack_damage_calculation(self):
        damage_list = []
        damage_list.append(Damage(DamageType.MAGIC, Dice(0, 0, self.get_intellect())))
        return damage_list
    
    def choose_target_for_attack(self, target_list):
        """Choose the target for an attack. In case of multiple targets choose the strongest one."""
        if not target_list:
            return None
        
        # One target, return it direcly
        if len(target_list) == 1:
            return target_list[0]
        
        # Multiple targets, return the strongest one
        target = max(target_list, key=lambda enemy: (enemy.get_max_hitpoints(), enemy.get_experience_points()))
        self.log_subject.notify_log_observer(f"Attacking {target.get_name()}")
        return target
    
    def base_attack(self):        
        attack_distance = 1
        close_up_enemies = self.game_panel.enemy_manager.get_close_up_enemies(attack_distance)
        target = self.choose_target_for_attack(close_up_enemies)
        if target is None:
            return
        else:
            super().attack(self.base_attack_damage_calculation(), target)
            self.set_actions_number(self.get_actions_number() + 1)
            self.set_take_turn(True)
        
    def spell_attack(self):
        if self.get_max_manapoints() == 0:
            self.log_subject.notify_log_observer(f"{self.warrior.get_warrior()} cannot cast a spell.")
            return
        
        manapoints_consumption = int(round(self.get_max_manapoints() * 0.05))
        if manapoints_consumption > self.get_manapoints():
            self.log_subject.notify_log_observer("Not enough manapoints to cast a spell.")
            return
        
        self.set_manapoints(self.get_manapoints() - manapoints_consumption)
        close_up_enemies = self.game_panel.enemy_manager.get_close_up_enemies(self.visibility_radius)
        target = self.choose_target_for_attack(close_up_enemies)
        if target is None:
            return
        else:
            super().attack(self.spell_attack_damage_calculation(), target)
            self.set_actions_number(self.get_actions_number() + 1)
            self.set_take_turn(True)

    def die(self):
        self.game_panel.set_game_over(True)

    def set_direction_before_moving(self, event):
        if event.key == pygame.K_w or event.key == pygame.K_UP:
            self.set_direction(Direction.UP)
        elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
            self.set_direction(Direction.DOWN)
        elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
            self.set_direction(Direction.LEFT)
        elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            self.set_direction(Direction.RIGHT)

    def check_for_enemy_collision(self, player_rect: pygame.Rect) -> bool:
        """Checks for player-enemy collisions."""
        enemy_manager = self.game_panel.enemy_manager
        for enemy in enemy_manager.get_generated_enemies():
            if player_rect.colliderect(enemy.get_rect()):
                return True
        return False

    def allowed_position(self):
        match self.get_direction():
            case Direction.UP:
                temp_rect = pygame.Rect(self.get_position().get_tile_x(), self.get_position().above().get_tile_y(), tile_size, tile_size)
            case Direction.DOWN:
                temp_rect = pygame.Rect(self.get_position().get_tile_x(), self.get_position().below().get_tile_y(), tile_size, tile_size)
            case Direction.LEFT:
                temp_rect = pygame.Rect(self.get_position().left().get_tile_x(), self.get_position().get_tile_y(), tile_size, tile_size)
            case Direction.RIGHT:
                temp_rect = pygame.Rect(self.get_position().right().get_tile_x(), self.get_position().get_tile_y(), tile_size, tile_size)
            case Direction.NONE:
                temp_rect = self.get_rect()

        collided = (
            self.check_for_wall_collision(temp_rect) or
            self.check_for_enemy_collision(temp_rect)
        )
        self.set_collision(collided)

    def move(self, event):
        # Opportunity attack variables
        close_distance = 1
        adjacent_enemies_before_move = self.game_panel.enemy_manager.get_close_up_enemies(close_distance)
        
        # Player movement logic
        self.set_direction_before_moving(event)
        self.allowed_position()
        if self.get_collision():
            return
        super().move()

        # Opportunity attack
        if adjacent_enemies_before_move:
            strongest_enemy = self.choose_target_for_attack(adjacent_enemies_before_move)
            if strongest_enemy.get_position().distance_to(self.get_position()) > close_distance:
                strongest_enemy.attack(opportunity_attack=True)

        self.set_take_turn(True)
        self.set_actions_number(self.get_actions_number() + 1)

    def actions(self, event):
        # If in item selection mode, route input to the correct handler
        if self.get_item_selection():
            if self.pending_equip_setter == self.set_main_hand:
                self.change_main_weapon(event)
            elif self.pending_equip_setter == self.set_off_hand:
                self.change_secondary_weapon(event)
            return

        # Movement
        movement_keys = [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]
        if event.key in movement_keys:
            self.move(event)

        # Attack
        if event.key == pygame.K_SPACE:
            self.base_attack()
        if event.key == pygame.K_x:
            self.spell_attack()

        # Beacon creation
        if event.key == pygame.K_l:
            self.create_beacon()

        # Potion consumption
        if event.key == pygame.K_h:
            self.consume_healing_potion()
        if event.key == pygame.K_m:
            self.consume_mana_potion()

        # Equip item
        if event.key == pygame.K_t:
            self.change_main_weapon(event)
        if event.key == pygame.K_y:
            self.change_secondary_weapon(event)
        if event.key == pygame.K_u:
            self.swap_weapons()
        
        # Rest
        if event.key == pygame.K_r:
            self.execute_rest()
    
    def reset_position(self):
        self.set_position(player_spawn)
        self.set_direction(Direction.NONE)
        self.update_rect()

    def reset_stats(self):
        self.set_level(1)
        self.set_experience_points(0)
        self.set_max_hitpoints(0)
        self.set_max_manapoints(0)
        self.race.init_stats(self)
        self.warrior.update_stats(self)
        self.set_hitpoints(self.get_max_hitpoints())
        self.set_manapoints(self.get_max_manapoints())

    def reset_equipment(self):
        self.warrior.set_starter_weapon(self)
        self.warrior.set_secondary_weapon(self)

    def restart(self):
        self.reset_position()
        self.reset_stats()
        self.reset_equipment()

        self.last_beacon_cast_action = -self.beacon_casting_cooldown
        self.last_rest_action = -self.resting_cooldown

        self.pending_equip_setter = None
        self.set_item_selection(False)
        self.set_actions_number(0)
        self.set_take_turn(False)

    def draw(self, display_surface: pygame.Surface):
        pygame.draw.rect(display_surface, player_color, self.get_rect())
        pygame.draw.rect(display_surface, (0, 0, 0), self.get_rect(), 1)