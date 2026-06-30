from __future__ import annotations

from dataclasses import dataclass
from typing import Any, AsyncIterator

import httpx


@dataclass(frozen=True)
class PokeAPIConfig:
    base_url: str = "https://pokeapi.co/api/v2"


class PokeAPIClient:
    """Async client stub for PokeAPI.

    Add endpoint-specific methods, pagination helpers, and response parsing as
    an exercise.
    """

    def __init__(self, config: PokeAPIConfig | None = None) -> None:
        self.config = config or PokeAPIConfig()
        self._client = httpx.AsyncClient(base_url=self.config.base_url)

    async def get_pokemon(self, name_or_id: str | int) -> dict[str, Any]:
        raise NotImplementedError

    async def list_pokemon(
        self,
        *,
        limit: int = 20,
        offset: int = 0,
    ) -> dict[str, Any]:
        raise NotImplementedError

    async def iter_pokemon(self, *, page_size: int = 100) -> AsyncIterator[dict[str, Any]]:
        raise NotImplementedError
        yield {}

    async def aclose(self) -> None:
        await self._client.aclose()

    async def __aenter__(self) -> "PokeAPIClient":
        return self

    async def __aexit__(self, *_exc: object) -> None:
        await self.aclose()
