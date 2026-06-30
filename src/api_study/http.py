from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import httpx


@dataclass(frozen=True)
class APIClientConfig:
    base_url: str
    timeout_seconds: float = 10.0


class APIClientError(Exception):
    """Base exception for API client failures."""


class APIRequestError(APIClientError):
    """Raised when an API request fails or returns an unexpected response."""


class AsyncBaseClient:
    """Small async HTTP client wrapper for exercises.

    API-specific clients should compose this class or copy the pattern, then add
    endpoint-specific methods, response parsing, authentication, and pagination.
    """

    def __init__(self, config: APIClientConfig) -> None:
        self.config = config
        self._client = httpx.AsyncClient(
            base_url=config.base_url,
            timeout=config.timeout_seconds,
        )

    async def get_json(self, path: str, **kwargs: Any) -> Any:
        raise NotImplementedError("Implement shared request/error handling as an exercise.")

    async def aclose(self) -> None:
        await self._client.aclose()

    async def __aenter__(self) -> "AsyncBaseClient":
        return self

    async def __aexit__(self, *_exc: object) -> None:
        await self.aclose()
