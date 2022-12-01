import random
import os
from time import sleep

import config

from cell import BaseCell
from life import Life


class Field:
    cells: dict = {}
    life_cells = {}

    def __init__(self):
        for row in range(config.H_FIELD_SIZE):
            for col in range(config.W_FIELD_SIZE):
                cell = BaseCell((row, col))
                Field.cells[(row, col)] = cell
        for _ in range(config.START_LIFE_CELLS):
            Field.born_random_cell()

    @staticmethod
    def born_random_cell():
        cell = Field.random_cell()
        cell.life_forms = Life()
        Field.life_cells[cell.position] = cell

    @staticmethod
    def random_cell():
        return Field.cells[(
            random.randint(0, config.H_FIELD_SIZE-1),
            random.randint(0, config.W_FIELD_SIZE-1)
        )]

    @staticmethod
    def draw():
        os.system('clear')
        frame = ''
        frame += '_' * (config.W_FIELD_SIZE * 2) + '\n'
        for row in range(config.H_FIELD_SIZE):
            frame += '|' + ' '.join([str(Field.cells[(row, col)]) for col in range(config.W_FIELD_SIZE)]) + '|' + '\n'
        frame += '_' * (config.W_FIELD_SIZE * 2) + '\n'
        print(frame)

    @staticmethod
    def _print():
        for key, val, in Field.cells.items():
            print(key, val)

    @staticmethod
    def run():
        while True:
            for living_cell in Field.life_cells:
                pass

            Field.draw()
            sleep(0.1)

