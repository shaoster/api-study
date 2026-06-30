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

## Project layout

```text
api-study/
├── apis/
│   ├── jsonplaceholder/
│   ├── openweathermap/
│   └── pokeapi/
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

## Suggested workflow for each exercise

1. Read the linked API docs for the target service.
2. Sketch the smallest useful client interface.
3. Implement request construction, error handling, and response parsing.
4. Add authentication handling if the API requires it.
5. Add pagination helpers for list/search endpoints.
6. Write tests using mocked HTTP responses before trying live calls.
7. Add a short usage example to the API folder README.
