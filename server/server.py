from basic import Basic

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import numpy as np

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/basic/1")
def basic1():
    b = Basic(-12, +12)
    method = np.random.choice(b.register())
    text, _ = method()
    problem = "{}".format(text)
    return {"problem": problem}


@app.get("/answer/{x}")
def answer(x):
    return {"hello": x}
