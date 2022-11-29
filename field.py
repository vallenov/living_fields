import config


class Field:
    cells = {}

    def __init__(self):
        for row in range(config.FIELD_SIZE):
            for col in range(config.FIELD_SIZE):
                cell = BaseCell()
                Field.cells[(row, col)] = cell

    @staticmethod
    def draw():
        print('_' * (config.FIELD_SIZE * 2))
        for row in range(config.FIELD_SIZE):
            print('|' + ' '.join([repr(Field.cells[(row, col)]) for col in range(config.FIELD_SIZE)]) + '|')
        print('_' * (config.FIELD_SIZE * 2))

    @staticmethod
    def _print():
        for key, val, in Field.cells.items():
            print(key, val)


class BaseCell:
    def __init__(self):
        self.look = '0'
        self.life_forms = []

    def __repr__(self):
        return self.look
