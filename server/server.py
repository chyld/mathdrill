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


@app.get("/basic/{basic_id}")
def basic1(basic_id: int):
    lookup = {1: (0, +12), 2: (0, +20), 3: (0, +100)}
    b = Basic(*lookup[basic_id])
    method = np.random.choice(b.register())
    question, answer = method()
    return {"question": question, "answer": answer.item()}
