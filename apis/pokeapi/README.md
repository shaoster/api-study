# PokeAPI Client Exercise

API docs: https://pokeapi.co/docs/v2

PokeAPI is useful for practicing unauthenticated API clients with pagination, linked resources, and nested response data.

## Client acceptance criteria

Build a Python client that can:

- fetch a Pokémon by name or ID
- list Pokémon with limit/offset pagination
- iterate through all pages using an async iterator or helper method
- follow linked resource URLs when appropriate
- normalize selected nested fields into a simpler Python shape
- expose async methods for IO-bound operations
- include tests that mock paginated responses

## API features to exercise

- offset-based pagination
- linked resources
- path parameters and flexible identifiers
- response parsing for nested JSON
- async iteration over paginated API results
