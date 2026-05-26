# FastAPI Interview Sandbox

A small FastAPI app for a ~15-minute live coding exercise during a technical interview.

## Setup

```bash
cd ./tech-interviews/python-dev
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Then open [http://localhost:8000/docs](http://localhost:8000/docs) for the interactive API browser.

## Your Task

Add a new endpoint: `**GET /users/{user_id}/transactions**`

### Requirements

1. Paginated response. Query params: `limit` (default 20, max 100) and `offset` (default 0).
2. Use Pydantic models for the response. Include a total count.
3. Return **404** if the user doesn't exist — match the pattern in `GET /users/{user_id}`.
4. Return **400 or 422** for invalid pagination params.
5. Add at least one pytest test covering the happy path and one covering the 404 case.

### Ground rules

- Use whatever AI tooling you'd normally use — Cursor, Claude Code, Copilot, anything.
- Narrate as you go. We're more interested in *how* you work with the tools than in finishing fast.
- It's fine to push back on the AI's output, regress and re-prompt, or write code by hand.
- If you finish early, walk us through what you'd refactor or harden for production.

## Running tests

```bash
pytest -v
```

## Files

- `main.py` — the API (your endpoint goes at the bottom)
- `test_main.py` — starter tests (extend it or add a new test file)
- `requirements.txt` — pinned dependencies

