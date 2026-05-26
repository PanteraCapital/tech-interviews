"""
FastAPI Sandbox — Technical Interview Exercise

Run locally:
    pip install fastapi uvicorn pytest httpx
    uvicorn main:app --reload

Then visit http://localhost:8000/docs

YOUR TASK:
    Add a new endpoint:  GET /users/{user_id}/transactions

    Requirements:
      1. Return a paginated list of transactions for the given user.
         - Query params:  limit (default 20, max 100) and offset (default 0).
      2. Use Pydantic models for the response. Include total count.
      3. Return 404 if the user doesn't exist (use the same pattern as
         GET /users/{user_id} below).
      4. Return 400 (or 422) for invalid pagination params.
      5. Write at least one pytest test covering the happy path AND
         the 404 case.

    Use your AI tooling however you normally would. Talk me through
    your prompts, what you accept, what you reject, and why.
"""

from datetime import datetime
from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Interview Sandbox API")


# ---------- Models ----------

class User(BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime


class Transaction(BaseModel):
    id: int
    user_id: int
    amount_cents: int
    currency: str
    description: str
    created_at: datetime


# ---------- Fake in-memory store ----------

USERS: dict[int, User] = {
    1: User(id=1, name="Ada Lovelace",   email="ada@example.com",
            created_at=datetime(2024, 1, 15, 9, 0)),
    2: User(id=2, name="Alan Turing",    email="alan@example.com",
            created_at=datetime(2024, 2, 20, 14, 30)),
    3: User(id=3, name="Grace Hopper",   email="grace@example.com",
            created_at=datetime(2024, 3, 5, 11, 45)),
}

# 50 transactions spread across the 3 users for pagination realism.
TRANSACTIONS: list[Transaction] = []
for i in range(1, 51):
    uid = ((i - 1) % 3) + 1
    TRANSACTIONS.append(Transaction(
        id=i,
        user_id=uid,
        amount_cents=1000 + (i * 137) % 9000,
        currency="USD",
        description=f"Transaction {i}",
        created_at=datetime(2024, 6, (i % 28) + 1, (i % 24), 0),
    ))


# ---------- Existing endpoints (reference patterns) ----------

@app.get("/")
def root():
    return {"status": "ok", "service": "interview-sandbox"}


@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    user = USERS.get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    return user


@app.get("/users", response_model=list[User])
def list_users():
    return list(USERS.values())


# ---------- ADD YOUR ENDPOINT BELOW ----------
#
# GET /users/{user_id}/transactions?limit=20&offset=0
#
# Response shape (suggested — feel free to tweak with reasoning):
#   {
#     "user_id": 1,
#     "total": 17,
#     "limit": 20,
#     "offset": 0,
#     "items": [ Transaction, Transaction, ... ]
#   }