from genotype import Genotype


class Life:
    def __init__(self):
        self.gen = Genotype()
        self.sprite = '0'

    def born(self):
        new_life = Life()
        new_life.gen = self.gen.mutation()
        return new_life


class Food:
    def __init__(self):
        self.gen = Genotype()
        self.sprite = '.'
