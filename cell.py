from typing import Optional
from life import Life


SPRITE = {
    'empty': ' ',
    'wall': 'П',
    'life': '0',
    'food': '.'
}


class BaseCell:
    def __init__(self, position: tuple):
        self.position = position
        self.look = SPRITE['empty']
        self.life_forms: Optional[Life] = None

    def __repr__(self):
        return f'{self.__class__}'

    def __str__(self):
        if self.life_forms:
            self.look = SPRITE['life']
        return self.look
