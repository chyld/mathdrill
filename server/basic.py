import numpy as np


class Basic:
    @staticmethod
    def register():
        return [Basic.addition, Basic.subtraction, Basic.multiplication]

    @staticmethod
    def addition():
        a, b = np.random.randint(-10, 10, 2)
        return "{} + {}".format(a, b), a + b

    @staticmethod
    def subtraction():
        a, b = np.random.randint(-10, 10, 2)
        return "{} - {}".format(a, b), a - b

    @staticmethod
    def multiplication():
        a, b = np.random.randint(-10, 10, 2)
        return "{} * {}".format(a, b), a * b
