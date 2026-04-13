# The Tower of Light

## Game Description

The objective of the game is to restore light to the tower, which is deeply immersed in Chaos. To accomplish this, the player needs to create three beacons of light on each level before unlocking the portal in the north-east corner of the map, which teleports them to the next level.
However, the path to the top won't be an easy one. Enemy forces are lurking in the shadows, gradually closing in on the player to stop them in their tracks. The player must battle these foes; while escaping is an option, it is definitely not a simple task.
In addition, with every beacon activated, the remaining enemies grow stronger, becoming more dangerous and ferocious. On the other hand, by successfully defeating enemies, the player progressively grows stronger and potentially gains access to precious loot, increasing their chances of survival.

## Controls

### Movement
- <kbd>W</kbd> / <kbd>&uarr;</kbd> : Move Up
- <kbd>S</kbd> / <kbd>&darr;</kbd> : Move Down
- <kbd>D</kbd> / <kbd>&rarr;</kbd> : Move Right
- <kbd>A</kbd> / <kbd>&larr;</kbd> : Move Left

### Resting
- <kbd>R</kbd> : Rest

### Spells
- <kbd>L</kbd> : Create Beacon of Light

### Attack
- <kbd>Space</kbd> : Melee Attack
- <kbd>X</kbd> : Magic Attack

### Inventory
- <kbd>T</kbd> : Change Main Weapon
- <kbd>Y</kbd> : Change Secondary Weapon
- <kbd>U</kbd> : Swap Weapons
- <kbd>H</kbd> : Consume Healing Potion
- <kbd>M</kbd> : Consume Mana Potion

## Game Content

### Player's Levels
The player levels up by gaining experience points via defeating enemies and creating beacons of light.

***Experience Points per Level***
| Level | Experience Points |
| :---: | :---: |
| 1 | 0 - 299|
| 2 | 300 - 899 |
| 3 | 900 - 2699 |
| 4 | 2700 - 6499 |
| 5 | 6500 - 13999 |
| 6 | 1400 - $\infty$ |

### Race
Each race is responsible for the inialization of the characters's base statistics.

***Base Statistics per Race***
| Race | Strength | Intellect | Swing Defense | Thrust Defense | Magic Defense |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Human  | 9  | 9  | 1 | 1 | 1 |
| Elf    | 6  | 12 | 0 | 1 | 2 |
| Orc    | 10 | 8  | 1 | 2 | 0 |
| Tauren | 12 | 6  | 1 | 2 | 0 |

### Warrior Class
Each warrior class is responsible for updating the character's statistics and determines the starter waepon.
***Progress' Statistics per Warrior Class***
| Warrior | Level | Max Hitpoints | Max Manapoints | Strength | Intellect |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Knight**  | 1 | +10 | +0   | +2  | +0  |
|             | 2 | +15 | +0   | +4  | +0  |
|             | 3 | +20 | +0   | +6  | +0  |
|             | 4 | +25 | +0   | +8  | +0  |
|             | 5 | +30 | +0   | +10 | +0  |
|             | 6 | +40 | +0   | +12 | +0  |
| **Mage**    | 1 | +8  | +12  | +2  | +8  |
|             | 2 | +12 | +40  | +3  | +16 |
|             | 3 | +16 | +60  | +4  | +24 |
|             | 4 | +20 | +80  | +5  | +32 |
|             | 5 | +24 | +100 | +6  | +40 |
|             | 6 | +30 | +120 | +7  | +48 |
| **Paladin** | 1 | +10 | +10  | +5  | +5  |
|             | 2 | +13 | +20  | +7  | +9  |
|             | 3 | +16 | +30  | +9  | +13 |
|             | 4 | +20 | +40  | +11 | +17 |
|             | 5 | +28 | +50  | +13 | +21 |
|             | 6 | +40 | +70  | +15 | +25 |

***Starting Weapon per Warrior Class***
| Warrior | Staring Weapon |
| :--- | :--- |
| Knight  | Wooden Sword |
| Mage    | Magic Wand   |
| Paladin | Spear        |

### Enemies
There are various enemies that appear on each level of the tower. The higher the tower level the stronger the enemies to be encountered.

***Statistics per Enemy***
| Enemy | Hitpoints | Swing Defense | Thrust Defense | Magic Defense | Experience Points | Weapon | Level Apperance |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- | :---: |
| Priest          | 20  | 0    | 0    | $\infty$ | 30  | Mace            | 1, 2    |
| Vampire         | 20  | 0    | 0    | $\infty$ | 30  | Dagger          | 1, 2    |
| Knight          | 30  | 3    | 3    | 1        | 50  | Blade of Light  | 2, 3, 4 |
| Chaos Knight    | 30  | 3    | 3    | 1        | 50  | Sword of Chaos  | 2, 3, 4 |
| Bishop          | 40  | 0    | 0    | 5        | 60  | Staff           | 2, 3, 4 |
| Summoner        | 40  | 0    | 0    | 5        | 60  | Summoning Stuff | 2, 3, 4 |
| Paladin         | 100 | 5    | 3    | 2        | 80  | Hammer of Wrath | 3, 4, 5 |
| Fallen Hero     | 100 | 5    | 3    | 2        | 80  | Ebon Blade      | 3, 4, 5 |
| Archangel       | 130 | 6    | 6    | 2        | 120 | Divine Hammer   | 4, 5, 6 |
| Fiend           | 130 | 6    | 6    | 2        | 200 | Demon Claws     | 5, 6    |
| Herald of Light | 160 | -50% | -50% | -50%     | 400 | Lightbringer    | 6       |
| Herald of Chaos | 160 | -50% | -50% | -50%     | 400 | Edge of Chaos   | 6       |

### Weapons
A weapon's statistics enhance the bearer's base attributes and determine the damage dealt in combat.

***Statistics per Weapon***
| Weapon | Swing Damage | Thrust Damage | Magical Damage | Manapoints Bonus | Strengh Bonus | Intellect Bonus |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Wooden Sword    | 1d3+1 | 0     | 0     | 0  | 0  | 0  |
| Magic Wand      | 1d3+0 | 0     | 1d3+1 | 0  | 0  | 0  |
| Spear           | 0     | 1d3+1 | 0     | 0  | 0  | 0  |
| Mace            | 1d6+1 | 0     | 0     | 0  | 0  | 0  |
| Dagger          | 0     | 1d6+1 | 0     | 0  | 0  | 0  |
| Blade of Light  | 0     | 2d6+1 | 1d3+0 | 0  | 0  | 0  |
| Sword of Chaos  | 0     | 2d6+1 | 1d3+0 | 0  | 0  | 0  |
| Staff           | 2d6+2 | 0     | 1d6+1 | 0  | 0  | 0  |
| Summoning Stuff | 2d6+2 | 0     | 1d6+1 | 0  | 0  | 0  |
| Hammer of Wrath | 2d6+1 | 0     | 1d6+1 | 0  | 0  | 0  |
| Ebon Blade      | 2d6+2 | 0     | 1d6+2 | 0  | 0  | 0  |
| Divine Hammer   | 0     | 2d6+4 | 2d6+2 | 0  | 0  | 0  |
| Demon Claws     | 2d6+4 | 0     | 2d6+2 | 0  | 0  | 0  |
| Lightbringer    | 1d6+2 | 3d6+2 | 1d6+2 | 10 | 10 | 10 |
| Edge of Chaos   | 1d6+2 | 3d6+2 | 1d6+2 | 10 | 10 | 10 |

#### Damage String Breakdown

The general format of a damage string is [num1]d[num2]+[num3], where:
- num1: The number of dice rolled.
- num2: The number of sides of each die.
- num3: A constant value added to the final result.
