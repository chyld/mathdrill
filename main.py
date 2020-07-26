from time import time

import numpy as np

# todo
#
# - change upper limit 1 to 100
# - change "n"
# - save to sql
# - multiplication
# - division
# - modularize
# - clear screen
# - add separate todo file


class Basic:
    @staticmethod
    def register():
        return [Basic.addition, Basic.subtraction]

    @staticmethod
    def addition():
        a, b = np.random.randint(1, 10, 2)
        return "{} + {}".format(a, b), a + b

    @staticmethod
    def subtraction():
        a, b = np.random.randint(1, 10, 2)
        return "{} - {}".format(a, b), a - b


class Train:
    def __init__(self, klass):
        self.klass = klass
        self.methods = klass.register()


n = 5
t = Train(Basic)
results = np.zeros(n)

for i in range(n):
    method = np.random.choice(t.methods)
    text, answer = method()
    start = time()
    while True:
        problem = "{} : {} > ".format(i, text)
        response = input(problem)
        if response == str(answer):
            break
    end = time()
    elapsed = end - start
    results[i] = elapsed

print("\nresults: {}".format(results.round(2)))
