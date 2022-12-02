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
                cell = BaseCell((col, row))
                Field.cells[(col, row)] = cell
        for position, cell in Field.cells.items():
            cell.neighbours = Field.add_neighbours(position)
        for _ in range(config.START_LIFE_CELLS):
            Field.born_random_cell()

    @staticmethod
    def add_neighbours(position: tuple):
        print(position)
        cur_c = position[0] - 1
        cur_r = position[1] - 1
        neighbours = []
        for i in range(1, 10):
            if Field.cells.get((cur_c, cur_r)) and (cur_c, cur_r) != position:
                neighbours.append(Field.cells[(cur_c, cur_r)])
            if not i % 3:
                cur_r += 1
                cur_c = position[0] - 1
            else:
                cur_c += 1
        return neighbours

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
        #os.system('clear')
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
            sleep(1)

