# API Study

Self-directed interview prep for live API coding interviews in Python.

This repository is a collection of small, intentionally unfinished client-building exercises for public web APIs. The goal is to practice the kinds of skills that often appear in live coding screens and take-home style API exercises:

- reading unfamiliar API documentation quickly
- designing a small Python client interface
- handling authentication when required
- supporting pagination and rate-limit-aware iteration
- writing async HTTP code where it improves ergonomics or throughput
- testing client behavior without depending on live third-party services
- separating API-specific logic from reusable HTTP/client infrastructure

## Recommended study path

Start with the API-specific folders under `apis/`. Those are meant for actual skills practice: reading docs, designing a client, handling authentication, adding pagination, and writing tests against mocked HTTP responses.

After you have built some muscle memory with the individual APIs, move to `prompts/` for interview grinding. Those prompts are intentionally blanker and more timeboxed so they feel closer to a live CoderPad screen: minimal setup, one focused problem, and just enough acceptance criteria to drive implementation.

In other words:

1. Use `apis/` to learn and practice the underlying API-client skills.
2. Use `prompts/` to rehearse applying those skills quickly under interview constraints.

## Project layout

```text
api-study/
├── apis/
│   ├── jsonplaceholder/
│   ├── openweathermap/
│   └── pokeapi/
├── prompts/
├── src/
│   └── api_study/
├── tests/
├── pyproject.toml
└── requirements-dev.txt
```

Each API folder contains:

- a `README.md` with API docs and acceptance criteria
- a `client.py` stub for the API-specific client
- a `test_client.py` stub for tests

The `prompts/` folder contains thinner CoderPad-style drills for timed repetition after the API-specific practice.

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

On Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

## Credentials and local secrets

Do not commit API keys, bearer tokens, cookies, or local credential files.

Use environment variables for credentials during normal development. For APIs that need secrets, create a local `.env` file at the repository root or an API-specific `.env` file inside that API folder, for example:

```text
.env
apis/openweathermap/.env
```

Example OpenWeatherMap value:

```bash
OPENWEATHERMAP_API_KEY=replace-me
```

The repository may include `.env.example` files showing variable names, but real `.env` files must stay local. The `.gitignore` is configured to ignore `.env`, `.env.*`, per-API `.env` files, and common local credential artifacts.

When writing clients, prefer reading credentials from environment variables, for example with `python-dotenv` during local development:

```python
from dotenv import load_dotenv

load_dotenv()
```

## Running checks

```bash
pytest
ruff check .
mypy src apis
```

## Suggested workflow for each API exercise

1. Read the linked API docs for the target service.
2. Sketch the smallest useful client interface.
3. Implement request construction, error handling, and response parsing.
4. Add authentication handling if the API requires it.
5. Add pagination helpers for list/search endpoints.
6. Write tests using mocked HTTP responses before trying live calls.
7. Add a short usage example to the API folder README.

## Suggested workflow for CoderPad-style prompts

1. Pick a prompt only after practicing the corresponding API folder.
2. Timebox yourself to 30–45 minutes.
3. Start from the minimal signature in the prompt or a blank file.
4. Implement only enough to satisfy the stated acceptance criteria.
5. Practice explaining tradeoffs and edge cases aloud as you code.
