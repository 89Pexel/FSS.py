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


class MinnowFish(Fish):
    def __init__(self):
        super().__init__(
            name = "Minnow",
            difficulty = 1,
            min_weight=0.1,
            max_weight=1.79,
            rarity = "common",
            zones = [0]
        )


class BlueGillFish(Fish):
    def __init__(self):
        super().__init__(
            name = "Blue Gill",
            difficulty = 1,
            min_weight=1.73,
            max_weight=4.8,
            rarity = "common",
            zones = [0]
        )


class PerchFish(Fish):
    def __init__(self):
        super().__init__(
            name = "Perch",
            difficulty = 0, 
            min_weight=0.1,
            max_weight=0.2,
            rarity = "common",
            zones = [0]
        )


class RoachFish(Fish):
    def __init__(self):
        super().__init__(
            name = "Roach",
            difficulty = 1,
            min_weight=2.2,
            max_weight=6.1,
            rarity = "uncommon",
            zones = [0]
        )


class KoiFish(Fish):
    def __init__(self):
        super().__init__(
            name = "Koi",
            difficulty = 2,
            min_weight=4.8,
            max_weight=10.3,    
            rarity = "rare",
            zones = [0]
        )

class ArowanaFish(Fish):
    def __init__(self):
        super().__init__(
            name = "Arowana",
            difficulty = 2,
            min_weight=9.4,
            max_weight=11.4,
            rarity = "epic",
            zones = [0]
        )

class TroutFish(Fish):
    def __init__(self):
        super().__init__(
            name = "Trout",
            difficulty = 0,
            min_weight=4.1,
            max_weight=10.0,
            rarity = "common",
            zones = [1]
        )

class CarpFish(Fish):
    def __init__(self):
        super().__init__(
            name = "Carp",
            difficulty = 2,
            min_weight=6.0,
            max_weight=9.4,
            rarity = "common",
            zones = [1]
        )

class PikeFish(Fish):
    def __init__(self):
        super().__init__(
            name = "Pike",
            difficulty = 2,
            min_weight=7.2,
            max_weight=10.3,
            rarity = "uncommon",
            zones = [1]
        )

class GarFish(Fish):
    def __init__(self):
        super().__init__(
            name = "Gar",
            difficulty = 3,
            min_weight=7.4,
            max_weight=11.9,
            rarity = "rare",
            zones = [1]
        )



class TrevallyFish(Fish):
    def __init__(self):
        super().__init__(
            name = "Trevally",
            difficulty = 4,
            min_weight=11.1,
            max_weight=14.3,
            rarity = "epic",
            zones = [1]
        )

class SnapperFish(Fish):
    def __init__(self):
        super().__init__(
            name = "Snapper",
            difficulty = 4,
            min_weight=11.7,
            max_weight=14.9,
            rarity = "common",
            zones = [2]
        )

class CodFish(Fish):
    def __init__(self):
        super().__init__(
            name = "Cod",
            difficulty = 4,
            min_weight=12.4,
            max_weight=16.4,
            rarity = "common",
            zones = [2]
        )

class BarracudaFish(Fish):
    def __init__(self):
        super().__init__(
            name = "Barracuda",
            difficulty = 4,
            min_weight=14.8,
            max_weight=20.7,
            rarity = "uncommon",
            zones = [2]
        )

class WahooFish(Fish):
    def __init__(self):
        super().__init__(
            name = "Wahoo",
            difficulty = 5,
            min_weight=17.4,
            max_weight=22.3,
            rarity = "rare",
            zones = [2]
        )

class SwordFishFish(Fish):
    def __init__(self):
        super().__init__(
            name = "Swordfish",
            difficulty = 5,
            min_weight=19.3,
            max_weight=24.4,
            rarity = "epic",
            zones = [2],
        )

class MahiMahiFish(Fish):
    def __init__(self):
        super().__init__(
        name="Mahi-Mahi",
        difficulty=5,
        min_weight=20.3,
        max_weight=25.7,
        rarity="epic",
        zones=[2]
    )

class KillifishFish(Fish):
    def __init__(self):
        super().__init__(
            name = "Killifish",
            difficulty = 6,
            min_weight = 19.8,
            max_weight = 28.4,
            rarity = "common",
            zones=[3]
    )

class BitterlingFish(Fish):
    def __init__(self):
        super().__init__(
            name = "Bitterling",
            difficulty = 6,
            min_weight = 20.4,
            max_weight = 29.7,
            rarity = "common",
            zones = [3]
        )

class SticklebackFish(Fish):
    def __init__(self):
        super().__init__(
            name = "Stickleback",
            difficulty = 6,
            min_weight = 24.7,
            max_weight = 27.4,
            rarity = "common",
            zones = [3]
    )


class ChimaeraFish(Fish):
    def __init__(self):
        super().__init__(
            name = "Chimaera",
            difficulty = 6,
            min_weight = 25.9,
            max_weight = 27.4,
            rarity = "uncommon",
            zones = [3]
        )


class ThaumatichthysFish(Fish):
    def __init__(self):
        super().__init__(
            name = "Thaumatichthys",
            difficulty = 7,
            min_weight = 29.6,
            max_weight = 34.4,
            rarity = "rare",
            zones = [3]
        )

class EurypharynxFish(Fish):
    def __init__(self):
        super().__init__(
            name = "Eurypharynx",
            difficulty = 7,
            min_weight = 32.9,
            max_weight = 35.9,
            rarity = "epic",
            zones = [3]
        )


class SaccopharynxFish(Fish):
    def __init__(self):
        super().__init__(
            name = "Saccopharynx",
            difficulty = 8,
            min_weight = 57.9,
            max_weight = 99.9,
            rarity = "legendary",
            zones = [3]
        )




all_fish = [
    MinnowFish(),
    BlueGillFish(),
    PerchFish(),
    RoachFish(),
    KoiFish(),
    ArowanaFish(),
    TroutFish(),
    CarpFish(),
    PikeFish(),
    GarFish(),
    TrevallyFish(),
    MahiMahiFish(),
    SwordFishFish(),
    WahooFish(),
    BarracudaFish(),
    CodFish(),
    SnapperFish(),
    KillifishFish(),
    BitterlingFish(),
    SticklebackFish(),
    ChimaeraFish(),
    ThaumatichthysFish(),
    EurypharynxFish(),
    SaccopharynxFish()
]
