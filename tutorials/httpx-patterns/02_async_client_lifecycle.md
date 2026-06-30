# 02: Async client lifecycle

The most important `httpx.AsyncClient` habit is to manage the client lifecycle explicitly.

## Minimal pattern

```python
import httpx


async def fetch_item(item_id: int) -> dict:
    async with httpx.AsyncClient(base_url="https://api.example.com") as client:
        response = await client.get(f"/items/{item_id}")
        response.raise_for_status()
        return response.json()
```

This is fine for tiny scripts and live interviews.

## Reusable client wrapper

For a real API client, create the HTTP client once and close it when done.

```python
import httpx


class ExampleClient:
    def __init__(self) -> None:
        self._client = httpx.AsyncClient(base_url="https://api.example.com")

    async def get_item(self, item_id: int) -> dict:
        response = await self._client.get(f"/items/{item_id}")
        response.raise_for_status()
        return response.json()

    async def aclose(self) -> None:
        await self._client.aclose()

    async def __aenter__(self) -> "ExampleClient":
        return self

    async def __aexit__(self, *_exc: object) -> None:
        await self.aclose()
```

Usage:

```python
async with ExampleClient() as client:
    item = await client.get_item(123)
```

## Practice task

Create a tiny client class for one API in this repo that:

- accepts `base_url` in `__init__`
- stores one `httpx.AsyncClient`
- exposes one async method
- supports `async with`
- closes cleanly

## Common mistakes

- Creating a new client for every request in production code.
- Forgetting to close the client.
- Mixing sync `httpx.Client` and async `httpx.AsyncClient` methods.
- Forgetting `await` on async calls.

## Interview talking point

In Go or Node, interviewers often expect explicit thinking about request lifecycle and cancellation. In Python, correct `AsyncClient` lifecycle is the equivalent signal.
