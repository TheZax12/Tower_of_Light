from __future__ import annotations

import random

class Dice:

    def __init__(self, dices_number: int, dice_sides_number: int, constant_addend: int):
        self.dices_number =  dices_number
        self.dice_sides_number = dice_sides_number
        self.constant_addend = constant_addend

    @classmethod
    def from_string(cls, dice_string: str) -> Dice:
        cleaned_dice_string = dice_string.strip().replace(" ", "")
        dice_part_1 = cleaned_dice_string.split('d')
        dices_number = int(dice_part_1[0])
        dice_part_2 = dice_part_1[1].split('+')
        dice_sides = int(dice_part_2[0])
        constant_addend = int(dice_part_2[1]) if len(dice_part_2) > 1 else 0
        return cls(dices_number, dice_sides, constant_addend)

    def add_constant_addend(self, value: int):
        self.constant_addend += value

    def roll(self) -> int:
        total_roll = sum(random.randint(1, self.dice_sides_number) for _ in range(self.dices_number))
        return total_roll + self.constant_addend
    
    def __repr__(self):
        return f"{self.dices_number}d{self.dice_sides_number}+{self.constant_addend}"
