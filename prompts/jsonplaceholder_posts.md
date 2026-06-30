# Drill: JSONPlaceholder Posts Client

Timebox: 30 minutes

Docs: https://jsonplaceholder.typicode.com/

## Task

Implement a small async Python client function that fetches posts from JSONPlaceholder.

Start from something like:

```python
async def fetch_posts(user_id: int | None = None) -> list[dict]:
    ...
```

## Requirements

- Fetch posts from `/posts`.
- When `user_id` is provided, send it as a query parameter.
- Return the decoded list of posts.
- Raise a clear exception for non-2xx responses.
- Keep the implementation small enough to explain aloud.

## Sample response shape

```json
[
  {
    "userId": 1,
    "id": 1,
    "title": "sample title",
    "body": "sample body"
  }
]
```

## Follow-up prompts an interviewer might add

- Add a method to fetch one post by ID.
- Validate that each post has `id`, `userId`, `title`, and `body`.
- Convert response dictionaries into a small dataclass.
- Add a retry for transient 5xx errors.

## Tests to consider

- Successful fetch without filters.
- Successful fetch with `user_id`.
- Non-2xx response raises your exception.
- Empty list response returns an empty list.
