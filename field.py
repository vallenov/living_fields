import random

import config

from cell import BaseCell
from life import Life


class Field:
    cells: dict = {}
    life_cells = {}

    def __init__(self):
        for row in range(config.FIELD_SIZE):
            for col in range(config.FIELD_SIZE):
                cell = BaseCell((row, col))
                Field.cells[(row, col)] = cell
        for _ in range(config.START_LIFE_CELLS):
            cell = self.random_cell()
            cell.life_forms.append(Life())
            Field.life_cells[cell.position] = cell

    @staticmethod
    def random_cell():
        return Field.cells[(
            random.randint(0, config.FIELD_SIZE-1),
            random.randint(0, config.FIELD_SIZE-1)
        )]

    @staticmethod
    def draw():
        print('_' * (config.FIELD_SIZE * 2))
        for row in range(config.FIELD_SIZE):
            print('|' + ' '.join([str(Field.cells[(row, col)]) for col in range(config.FIELD_SIZE)]) + '|')
        print('_' * (config.FIELD_SIZE * 2))

    @staticmethod
    def _print():
        for key, val, in Field.cells.items():
            print(key, val)

