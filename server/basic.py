from greek import alphabet

import numpy as np


class Basic:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper + 1

    def register(self):
        return [
            self.addition,
            self.subtraction,
            self.multiplication,
            self.modulus]

    def get_values(self):
        return np.random.randint(self.lower, self.upper, 2)

    def get_greek(self):
        return np.random.choice(alphabet)

    def addition(self):
        a, b = self.get_values()
        return "{} = ({}) + ({})".format(self.get_greek(), a, b), a + b

    def subtraction(self):
        a, b = self.get_values()
        return "{} = ({}) - ({})".format(self.get_greek(), a, b), a - b

    def multiplication(self):
        a, b = self.get_values()
        return "{} = ({}) ({})".format(self.get_greek(), a, b), a * b

    def modulus(self):
        while True:
            a, b = self.get_values()
            if a > 0 and b > 0:
                break
        return "{} = ({}) mod ({})".format(self.get_greek(), a, b), a % b
