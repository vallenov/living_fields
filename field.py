import random
import os
from time import sleep

import config

from cell import BaseCell
from life import Life, Food


class Field:
    cells: dict = {}
    life_cells: dict = {}
    food: dict = {}

    def __init__(self):
        for row in range(config.H_FIELD_SIZE):
            for col in range(config.W_FIELD_SIZE):
                cell = BaseCell((col, row))
                Field.cells[(col, row)] = cell
        for position, cell in Field.cells.items():
            cell.neighbours = Field.add_neighbours(position)
        for _ in range(config.START_LIFE_CELLS):
            Field.born_random_cell()
        for _ in range(config.START_FOOD):
            Field.born_random_food()

    @staticmethod
    def add_neighbours(position: tuple):
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
    def born_random_food():
        cell = Field.random_cell()
        cell.content = Food()
        Field.food[cell.position] = cell

    @staticmethod
    def born_random_cell():
        cell = Field.random_cell()
        cell.content = Life()
        Field.life_cells[cell.position] = cell

    @staticmethod
    def random_cell():
        return Field.cells[(
            random.randint(0, config.W_FIELD_SIZE-1),
            random.randint(0, config.H_FIELD_SIZE-1)
        )]

    @staticmethod
    def draw():
        os.system('clear')
        frame = ''
        frame += '_' * (config.W_FIELD_SIZE * 2) + '\n'
        for row in range(config.H_FIELD_SIZE):
            frame += '|' + ' '.join([str(Field.cells[(col, row)]) for col in range(config.W_FIELD_SIZE)]) + '|' + '\n'
        frame += '_' * (config.W_FIELD_SIZE * 2) + '\n'
        print(frame)

    @staticmethod
    def run():
        flag = 0
        buffer = list(Field.life_cells.values())
        while True:
            if flag == len(buffer):
                Field.draw()
                flag = 0
                sleep(0.1)
            print(buffer)
            current_cell = buffer.pop(0)
            current_cell.content.gen.start_energy.value -= 1
            if not current_cell.content.gen.start_energy.value:
                Field.cells[current_cell.position].content = None
                continue
            neighbour_food = [cell for cell in current_cell.neighbours if isinstance(cell, Food)]
            rand_neighbour = None
            if neighbour_food:
                rand_neighbour = random.choice(neighbour_food)
            if not rand_neighbour:
                rand_neighbour = random.choice(current_cell.neighbours)
            if isinstance(rand_neighbour.content, Life):
                buffer.append(current_cell)
                continue
            elif isinstance(rand_neighbour.content, Food):
                current_cell.content.gen.start_energy.value += 100
                buffer.append(rand_neighbour)
            Field.cells[rand_neighbour.position].content = current_cell.content
            Field.cells[current_cell.position].content = None
            flag += 1

