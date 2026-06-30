# Drill: PokeAPI Pagination

Timebox: 45 minutes

Docs: https://pokeapi.co/docs/v2

## Task

Implement an async helper that returns Pokémon names across paginated PokeAPI results.

Start from something like:

```python
async def list_pokemon_names(limit: int = 100) -> list[str]:
    ...
```

## Requirements

- Fetch from `/pokemon`.
- Use `limit` and `offset` query parameters.
- Continue until there are no more pages.
- Return only the Pokémon names, in API order.
- Raise a clear exception for non-2xx responses.
- Avoid recursion; use a loop.

## Sample response shape

```json
{
  "count": 3,
  "next": "https://pokeapi.co/api/v2/pokemon?offset=2&limit=2",
  "previous": null,
  "results": [
    {"name": "bulbasaur", "url": "https://pokeapi.co/api/v2/pokemon/1/"},
    {"name": "ivysaur", "url": "https://pokeapi.co/api/v2/pokemon/2/"}
  ]
}
```

## Follow-up prompts an interviewer might add

- Stop after `max_items` results.
- Yield names with an async iterator instead of returning a list.
- Fetch details for each Pokémon concurrently with a concurrency limit.
- Preserve useful error details from failed responses.

## Tests to consider

- One-page response.
- Multi-page response.
- Empty result set.
- Non-2xx response raises your exception.
- Final partial page is handled correctly.
