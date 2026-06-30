import pytest

from client import OpenWeatherMapClient


@pytest.mark.asyncio
async def test_current_weather_stub() -> None:
    client = OpenWeatherMapClient()
    with pytest.raises(NotImplementedError):
        await client.get_current_weather_by_city("San Francisco", units="imperial")
    await client.aclose()
