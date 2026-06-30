import pytest

from client import PokeAPIClient


@pytest.mark.asyncio
async def test_get_pokemon_stub() -> None:
    client = PokeAPIClient()
    with pytest.raises(NotImplementedError):
        await client.get_pokemon("pikachu")
    await client.aclose()
