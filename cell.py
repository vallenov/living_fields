import random
from typing import Optional, Any
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
        self.content: Optional[Any] = None
        self.neighbours: Optional[list] = []

    def __repr__(self):
        return f'{self.__class__}'

    def __str__(self):
        if not self.content:
            self.look = SPRITE['empty']

        else:
            self.look = self.content.sprite
        return self.look
