# 01: Quickstart basics

Official reference: https://www.python-httpx.org/quickstart/

This lesson mirrors the first half of the HTTPX quickstart: request verbs, URL parameters, response content, headers, and request bodies.

## Basic requests

HTTPX top-level calls should feel familiar if you know `requests`.

```python
import httpx

r = httpx.get("https://httpbin.org/get")
r = httpx.post("https://httpbin.org/post", data={"key": "value"})
r = httpx.put("https://httpbin.org/put", data={"key": "value"})
r = httpx.delete("https://httpbin.org/delete")
```

## Query parameters

```python
params = {"key1": "value1", "key2": ["value2", "value3"]}
r = httpx.get("https://httpbin.org/get", params=params)
```

Practice inspecting `r.url` so you can see how repeated query parameters are encoded.

## Response content

```python
r = httpx.get("https://www.example.org/")
text_body = r.text
raw_body = r.content
```

For APIs, JSON is usually the main path:

```python
r = httpx.get("https://api.github.com/events")
data = r.json()
```

## Custom headers

```python
headers = {"user-agent": "api-study/0.1"}
r = httpx.get("https://httpbin.org/headers", headers=headers)
```

## Request bodies

Form-encoded data:

```python
r = httpx.post("https://httpbin.org/post", data={"key": "value"})
```

JSON data:

```python
payload = {"integer": 123, "boolean": True, "items": ["a", "b"]}
r = httpx.post("https://httpbin.org/post", json=payload)
```

Multipart files:

```python
with open("report.txt", "rb") as f:
    r = httpx.post("https://httpbin.org/post", files={"upload-file": f})
```

Binary content:

```python
r = httpx.post("https://httpbin.org/post", content=b"hello")
```

## Practice task

Write a small script that makes one request for each shape above:

- GET with query params
- GET with custom headers
- POST with form data
- POST with JSON data
- POST with binary data

For each request, print or inspect:

- `r.status_code`
- `r.url`
- `r.headers.get("content-type")`
- one value from `r.json()` when the response is JSON

## Interview talking points

- Use `params` for query strings rather than manually concatenating URLs.
- Use `json` for JSON bodies and `data` for form bodies.
- Prefer explicit headers over hidden global state.
- Keep request construction easy to inspect and test.
