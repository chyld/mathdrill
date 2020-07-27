from fastapi import FastAPI
# from time import time
from basic import Basic
import numpy as np
from train import Train

app = FastAPI()

t = Train(Basic)


@app.get("/")
def home():
    method = np.random.choice(t.methods)
    text, _ = method()
    problem = "{}".format(text)
    return {"problem": problem}
