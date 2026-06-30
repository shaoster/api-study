# 01: From requests to httpx

`httpx` intentionally feels familiar if you know `requests`, but it supports both synchronous and asynchronous clients.

## Familiar synchronous shape

```python
import httpx

response = httpx.get(
    "https://api.example.com/items",
    params={"limit": 10},
    timeout=10.0,
)
response.raise_for_status()
data = response.json()
```

This is close to:

```python
import requests

response = requests.get(
    "https://api.example.com/items",
    params={"limit": 10},
    timeout=10.0,
)
response.raise_for_status()
data = response.json()
```

## Prefer a reusable client

For real client code, prefer a reusable client object instead of top-level request functions.

```python
import httpx

with httpx.Client(base_url="https://api.example.com") as client:
    response = client.get("/items", params={"limit": 10})
    response.raise_for_status()
    data = response.json()
```

## Async version

```python
import httpx

async with httpx.AsyncClient(base_url="https://api.example.com") as client:
    response = await client.get("/items", params={"limit": 10})
    response.raise_for_status()
    data = response.json()
```

## Practice task

Take a small `requests.get(...)` snippet and rewrite it three ways:

1. top-level `httpx.get(...)`
2. `httpx.Client(...)`
3. `httpx.AsyncClient(...)`

Keep the behavior the same: URL, params, timeout, status handling, and JSON decoding.

## Interview talking points

- Top-level calls are convenient but hide client lifecycle.
- Reusable clients can reuse connections.
- Async clients require `await` and an event loop.
- A Python async client maps more naturally to Node-style async/await and Go-style concurrent IO thinking.
