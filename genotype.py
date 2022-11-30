import random

from typing import Optional

__all__ = [
    'Genotype'
]


class Genotype:
    def __init__(self):
        self.weight = Weight(random.randint(10, 16))
        self.speed = Speed(random.randint(8, 10)),
        self.sight_distance = SightDistance(random.randint(200, 400)),
        self.anger = Anger(random.randint(0, 100)),
        self.max_energy = MaxEnergy(random.randint(800, 1500)),
        self.birth_losses = BirthLosses(random.randint(600, 800)),
        self.energy_for_born = EnergyForBorn(random.randint(600, 800)),
        self.run_chance = RunChance(random.randint(0, 30)),
        self.start_energy = StartEnergy(random.randint(400, 700))

    def _all_gen(self):
        return [
            self.weight,
            self.speed,
            self.sight_distance,
            self.anger,
            self.max_energy,
            self.birth_losses,
            self.energy_for_born,
            self.run_chance,
            self.start_energy
        ]

    def mutation(self):
        new_genotype = Genotype()
        new_genotype.size = self.weight.mutation()
        return new_genotype


class Gen:
    min_value: Optional[int]
    max_value: Optional[int]
    map: dict
    sorted_map_keys: dict

    def __init__(self, value):
        self.value = self.min_value if not value else value

    def __repr__(self):
        return f'<{type(self).__name__} {self.value}>'

    def new_value(self, val=None):
        rand = random.randint(0, 100)
        diff = 0
        for k in self.sorted_map_keys:
            diff = self.map[k]
            if k > rand:
                diff = self.map[k]
                break
        diff = random.choice([diff, -diff])
        new_val = None
        val = self.value if val is None else val
        if self.min_value <= val + diff <= self.max_value:
            new_val = val + diff
        elif val + diff >= self.max_value:
            new_val = self.max_value
        elif val + diff <= self.min_value:
            new_val = self.min_value
        return new_val


class Weight(Gen):
    min_value = 10
    max_value = 100
    map = {
        10: 10,
        20: 8,
        30: 5,
        40: 3,
        60: 2,
        90: 1
    }
    sorted_map_keys = sorted(map.keys())

    def mutation(self):
        return Weight(self.new_value())


class Speed(Gen):
    min_value = 10
    max_value = 40
    map = {
        10: 6,
        20: 5,
        30: 4,
        40: 3,
        60: 2,
        90: 1
    }
    sorted_map_keys = sorted(map.keys())

    def mutation(self):
        return Speed(super().new_value())


class SightDistance(Gen):
    min_value = 200
    max_value = 400
    map = {
        1: 3,
        10: 2,
        50: 1
    }
    sorted_map_keys = sorted(map.keys())

    def mutation(self):
        return SightDistance(super().new_value())


class Anger(Gen):
    min_value = 0
    max_value = 100
    map = {
        1: 10,
        3: 8,
        10: 5,
        30: 3,
        40: 2,
        50: 1
    }
    sorted_map_keys = sorted(map.keys())

    def mutation(self):
        return Anger(super().new_value())


class MaxEnergy(Gen):
    min_value = 800
    max_value = 2000
    map = {
        1: 70,
        3: 60,
        10: 50,
        30: 40,
        40: 30,
        50: 10
    }
    sorted_map_keys = sorted(map.keys())

    def mutation(self):
        return MaxEnergy(super().new_value())


class BirthLosses(Gen):
    min_value = 600
    max_value = MaxEnergy.min_value
    map = {
        1: 70,
        3: 60,
        10: 30,
        30: 15,
        40: 10,
        50: 5
    }
    sorted_map_keys = sorted(map.keys())

    def mutation(self):
        return BirthLosses(super().new_value())


class EnergyForBorn(Gen):
    min_value = 700
    max_value = 1500
    map = {
        1: 70,
        3: 60,
        10: 30,
        30: 15,
        40: 10,
        50: 5
    }
    sorted_map_keys = sorted(map.keys())

    def mutation(self):
        return EnergyForBorn(super().new_value())


class RunChance(Gen):
    min_value = 0
    max_value = 70
    map = {
        1: 20,
        3: 15,
        10: 8,
        30: 3,
        40: 2,
        50: 1
    }
    sorted_map_keys = sorted(map.keys())

    def mutation(self):
        return RunChance(super().new_value())


class StartEnergy(Gen):
    min_value = 400
    max_value = 700
    map = {
        1: 200,
        3: 150,
        10: 80,
        30: 30,
        40: 20,
        50: 10
    }
    sorted_map_keys = sorted(map.keys())

    def mutation(self):
        return StartEnergy(super().new_value())
