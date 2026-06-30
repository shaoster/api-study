# HTTPX Quickstart Patterns for API Interview Prep

This tutorial folder is deliberately convergent with the official HTTPX quickstart: https://www.python-httpx.org/quickstart/

Use the official page as the source of truth, then use these notes to practice the same patterns in an interview-prep style. The emphasis is on becoming fluent with HTTPX while still connecting it back to what you already know from `requests`.

Many companies that use Go or Node expect candidates to be comfortable thinking in terms of concurrent IO, request lifecycles, timeouts, and explicit error handling. `httpx.AsyncClient` is a good Python way to practice those patterns while staying in Python.

## Suggested order

1. `01_quickstart_basics.md` — verbs, params, response content, JSON, headers, and request bodies.
2. `02_status_headers_timeouts_auth.md` — status codes, response headers, redirects, timeouts, auth, and exceptions.
3. `03_async_quickstart_equivalents.md` — convert the same quickstart patterns to `AsyncClient`.
4. `04_clients_pagination_and_concurrency.md` — use reusable clients, pagination loops, and bounded concurrency.
5. `05_testing_httpx_clients.md` — test async clients with mocked responses.

## Practice goal

After this section, you should be able to explain and implement:

- top-level HTTPX request calls that look similar to `requests`
- query parameters with `params=...`
- response handling with `.text`, `.content`, and `.json()`
- custom headers
- form, JSON, multipart, and binary request bodies
- status-code checks with `raise_for_status()`
- response-header inspection
- redirect behavior with `follow_redirects=True`
- timeout configuration
- basic and digest authentication
- explicit handling of `RequestError` versus `HTTPStatusError`
- async equivalents using `httpx.AsyncClient`
- bounded concurrent requests with `asyncio.Semaphore`
- mocked tests that avoid live network calls

## Interview framing

In a Python interview, async may not be required. But practicing with `httpx` helps you speak the same language as async-native stacks:

- Node: promises, `fetch`, async/await, request concurrency
- Go: goroutines, contexts, timeouts, HTTP clients
- Python: `asyncio`, `httpx.AsyncClient`, cancellation-aware IO

The underlying interview skill is not the library. It is making external API calls safely, clearly, and testably.
