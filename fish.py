import time
import sys
import random


class Fish:
    def __init__(self, difficulty, min_weight, max_weight, name, rarity, zones):
        self.name = name
        self.difficulty = difficulty
        self.min_weight = min_weight
        self.max_weight = max_weight
        self.weight = random.uniform(min_weight, max_weight)
        self.rarity = rarity
        self.zones = zones


class ButterDoggyFish(Fish):
    def __init__(self):
        super().__init__(
            name = "Butter Doggy",
            difficulty = 1,
            min_weight=0.1,
            max_weight=1.79,
            rarity = "common",
            zones = [0]
        )


class ChickyFish(Fish):
    def __init__(self):
        super().__init__(
            name = "Chicky",
            difficulty = 1,
            min_weight=1.73,
            max_weight=4.8,
            rarity = "common",
            zones = [0]
        )


class WhiteteddyFish(Fish):
    def __init__(self):
        super().__init__(
            name = "Whiteteddy",
            difficulty = 0, 
            min_weight=0.1,
            max_weight=0.2,
            rarity = "common",
            zones = [0]
        )


class DoggyFish(Fish):
    def __init__(self):
        super().__init__(
            name = "Doggy",
            difficulty = 1,
            min_weight=2.2,
            max_weight=6.1,
            rarity = "uncommon",
            zones = [0]
        )


class WhaleyFish(Fish):
    def __init__(self):
        super().__init__(
            name = "Whaley",
            difficulty = 2,
            min_weight=4.8,
            max_weight=10.3,    
            rarity = "rare",
            zones = [0]
        )

class TeddyFish(Fish):
    def __init__(self):
        super().__init__(
            name = "Teddy",
            difficulty = 2,
            min_weight=9.4,
            max_weight=11.4,
            rarity = "epic",
            zones = [0]
        )

class MushroomFish(Fish):
    def __init__(self):
        super().__init__(
            name = "Mushroom",
            difficulty = 0,
            min_weight=4.1,
            max_weight=10.0,
            rarity = "common",
            zones = [1]
        )

class MallowFish(Fish):
    def __init__(self):
        super().__init__(
            name = "Mallow",
            difficulty = 2,
            min_weight=6.0,
            max_weight=9.4,
            rarity = "common",
            zones = [1]
        )

class MrLeastsNuggetFish(Fish):
    def __init__(self):
        super().__init__(
            name = "Mr Leasts Nuggets",
            difficulty = 2,
            min_weight=7.2,
            max_weight=10.3,
            rarity = "uncommon",
            zones = [1]
        )

class ChickyNuggetFish(Fish):
    def __init__(self):
        super().__init__(
            name = "Chicky Nuggets",
            difficulty = 3,
            min_weight=7.4,
            max_weight=11.9,
            rarity = "rare",
            zones = [1]
        )



class BearyTriangleFish(Fish):
    def __init__(self):
        super().__init__(
            name = "Beary Triangle",
            difficulty = 4,
            min_weight=11.1,
            max_weight=14.3,
            rarity = "epic",
            zones = [1]
        )

class ChipFish(Fish):
    def __init__(self):
        super().__init__(
            name = "Chip",
            difficulty = 4,
            min_weight=11.7,
            max_weight=14.9,
            rarity = "common",
            zones = [2]
        )

class BurgerFish(Fish):
    def __init__(self):
        super().__init__(
            name = "Burger",
            difficulty = 4,
            min_weight=12.4,
            max_weight=16.4,
            rarity = "common",
            zones = [2]
        )

class PizzaFish(Fish):
    def __init__(self):
        super().__init__(
            name = "Pizza",
            difficulty = 4,
            min_weight=14.8,
            max_weight=20.7,
            rarity = "uncommon",
            zones = [2]
        )

class KFCFish(Fish):
    def __init__(self):
        super().__init__(
            name = "KFC",
            difficulty = 5,
            min_weight=17.4,
            max_weight=22.3,
            rarity = "rare",
            zones = [2]
        )

class JunkFish(Fish):
    def __init__(self):
        super().__init__(
            name = "Junk Fish",
            difficulty = 5,
            min_weight=19.3,
            max_weight=24.4,
            rarity = "epic",
            zones = [2],
        )

class EnergyDrinkFish(Fish):
    def __init__(self):
        super().__init__(
        name="Energy Drink",
        difficulty=5,
        min_weight=20.3,
        max_weight=25.7,
        rarity="epic",
        zones=[2]
    )

all_fish = [
    ButterDoggyFish(),
    ChickyFish(),
    WhiteteddyFish(),
    DoggyFish(),
    WhaleyFish(),
    TeddyFish(),
    MushroomFish(),
    MallowFish(),
    MrLeastsNuggetFish(),
    ChickyNuggetFish(),
    BearyTriangleFish(),
    ChipFish(),
    BurgerFish(),
    PizzaFish(),
    KFCFish(),
    JunkFish(),
    EnergyDrinkFish(),
]