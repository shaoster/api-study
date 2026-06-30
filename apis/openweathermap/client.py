from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import httpx


@dataclass(frozen=True)
class OpenWeatherMapConfig:
    base_url: str = "https://api.openweathermap.org"
    api_key_env_var: str = "OPENWEATHERMAP_API_KEY"


class OpenWeatherMapClient:
    """Async client stub for OpenWeatherMap.

    Add authentication, request construction, response parsing, and error
    handling as an exercise.
    """

    def __init__(self, config: OpenWeatherMapConfig | None = None) -> None:
        self.config = config or OpenWeatherMapConfig()
        self._client = httpx.AsyncClient(base_url=self.config.base_url)

    async def get_current_weather_by_city(
        self,
        city: str,
        *,
        units: str | None = None,
    ) -> dict[str, Any]:
        raise NotImplementedError

    async def get_current_weather_by_coordinates(
        self,
        latitude: float,
        longitude: float,
        *,
        units: str | None = None,
    ) -> dict[str, Any]:
        raise NotImplementedError

    async def aclose(self) -> None:
        await self._client.aclose()

    async def __aenter__(self) -> "OpenWeatherMapClient":
        return self

    async def __aexit__(self, *_exc: object) -> None:
        await self.aclose()
