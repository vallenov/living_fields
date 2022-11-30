import random

from typing import Optional, Any


class Genotype:
    def __init__(self):
        self.energy: Optional[int]
        self.speed: Optional[int]
        self.straight: Optional[int]
        self.weight: Optional[int]

    @staticmethod
    def mutation():
        new_genotype = Genotype()
        new_genotype.speed += random.randint(-1, 1) if new_genotype.speed else 0
        return new_genotype


class Gen:
    min_value: Optional[int]
    max_value: Optional[int]
    map: dict
    sorted_map_keys: dict

    def __init__(self):
        self.value = None

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
