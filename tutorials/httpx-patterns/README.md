# httpx Patterns for API Interview Prep

This tutorial folder is for practicing Python API-client patterns with `httpx`, especially if you are already comfortable with `requests` but want more fluency with async-native workflows.

Many companies that use Go or Node expect candidates to be comfortable thinking in terms of concurrent IO, request lifecycles, cancellation/timeouts, and explicit error handling. `httpx.AsyncClient` is a good Python way to practice those patterns while staying in Python.

## Suggested order

1. `01_requests_to_httpx.md` — map familiar `requests` patterns to `httpx`.
2. `02_async_client_lifecycle.md` — use `AsyncClient` correctly.
3. `03_timeouts_errors_retries.md` — handle API failures without hiding useful context.
4. `04_concurrency_limits.md` — run concurrent requests without stampeding an API.
5. `05_testing_httpx_clients.md` — test async clients with mocked responses.

## Practice goal

After this section, you should be able to explain and implement:

- when to use `httpx.Client` versus `httpx.AsyncClient`
- why client reuse matters
- how to structure `async with httpx.AsyncClient(...)`
- how to add params, headers, auth, and JSON bodies
- how to configure timeouts
- how to handle HTTP status errors and network errors separately
- how to paginate with a loop
- how to run bounded concurrent requests with `asyncio.Semaphore`
- how to test without live network calls

## Interview framing

In a Python interview, async may not be required. But practicing with `httpx` helps you speak the same language as async-native stacks:

- Node: promises, `fetch`, async/await, request concurrency
- Go: goroutines, contexts, timeouts, HTTP clients
- Python: `asyncio`, `httpx.AsyncClient`, cancellation-aware IO

The underlying interview skill is not the library. It is making external API calls safely, clearly, and testably.
