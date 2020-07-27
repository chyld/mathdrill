import numpy as np


class Basic:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper + 1

    def register(self):
        return [self.addition, self.subtraction, self.multiplication]

    def get_values(self):
        return np.random.randint(self.lower, self.upper, 2)

    def addition(self):
        a, b = self.get_values()
        return "{} + {}".format(a, b), a + b

    def subtraction(self):
        a, b = self.get_values()
        return "{} - {}".format(a, b), a - b

    def multiplication(self):
        a, b = self.get_values()
        return "{} * {}".format(a, b), a * b
