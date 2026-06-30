import pytest

from client import JSONPlaceholderClient


@pytest.mark.asyncio
async def test_get_post_stub() -> None:
    client = JSONPlaceholderClient()
    with pytest.raises(NotImplementedError):
        await client.get_post(1)
    await client.aclose()
