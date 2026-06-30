from pathlib import Path


def test_expected_api_exercise_folders_exist() -> None:
    root = Path(__file__).resolve().parents[1]
    for folder in ["jsonplaceholder", "openweathermap", "pokeapi"]:
        assert (root / "apis" / folder / "README.md").exists()
        assert (root / "apis" / folder / "client.py").exists()
        assert (root / "apis" / folder / "test_client.py").exists()
