from basic import Basic

from fastapi import FastAPI

import numpy as np

app = FastAPI()


@app.get("/basic/1")
def basic1():
    b = Basic(-12, +12)
    method = np.random.choice(b.register())
    text, _ = method()
    problem = "{}".format(text)
    return {"problem": problem}
