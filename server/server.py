from time import time

from basic import Basic

from data import Data

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
db = Data()


@app.get("/basic/{basic_id}")
def basic1(basic_id: int):
    lookup = {1: (0, +12), 2: (0, +20), 3: (0, +100)}
    b = Basic(*lookup[basic_id])
    method = np.random.choice(b.register())
    question, answer = method()
    drill_id = db.create(f"/basic/{basic_id}", question, answer)
    return {"drill_id": drill_id, "question": question}


@app.put("/attempt/{drill_id}/{response}")
def answer(drill_id: int, response: int):
    result = db.find_by_id(drill_id)
    if isinstance(result, tuple):
        drill_id, _, _, answer, start_time, _, _ = result
        status = response == answer
        start_time = float(start_time)
        stop_time = time()
        elapsed = int(stop_time - start_time)
        if status:
            db.finsh(drill_id, stop_time, elapsed)
        return {"status": status, "elapsed": elapsed}
    else:
        return {"status": False}
