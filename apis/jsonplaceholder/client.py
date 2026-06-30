from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import httpx


@dataclass(frozen=True)
class JSONPlaceholderConfig:
    base_url: str = "https://jsonplaceholder.typicode.com"


class JSONPlaceholderClient:
    """Async client stub for JSONPlaceholder.

    Add endpoint-specific methods as an exercise. Keep API-specific logic here,
    not in the shared infrastructure package.
    """

    def __init__(self, config: JSONPlaceholderConfig | None = None) -> None:
        self.config = config or JSONPlaceholderConfig()
        self._client = httpx.AsyncClient(base_url=self.config.base_url)

    async def get_post(self, post_id: int) -> dict[str, Any]:
        raise NotImplementedError

    async def list_posts(self, *, user_id: int | None = None) -> list[dict[str, Any]]:
        raise NotImplementedError

    async def aclose(self) -> None:
        await self._client.aclose()

    async def __aenter__(self) -> "JSONPlaceholderClient":
        return self

    async def __aexit__(self, *_exc: object) -> None:
        await self.aclose()
