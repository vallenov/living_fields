import random
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
        self.position: Optional[tuple] = position
        self.look: Optional[str] = SPRITE['empty']
        self.life_form: Optional[Life] = None
        self.neighbours: Optional[list] = []

    def __repr__(self):
        return f'{self.__class__}'

    def __str__(self):
        if self.life_form:
            self.look = SPRITE['life']
        else:
            self.look = SPRITE['empty']
        return self.look
