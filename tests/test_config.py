from app.config import Settings


def test_database_url_defaults_to_local_postgres(monkeypatch):
    monkeypatch.delenv("DATABASE_URL", raising=False)

    settings = Settings(_env_file=None)

    assert settings.database_url.startswith("postgresql+psycopg://")


def test_database_url_is_read_from_environment(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "sqlite:///test.db")

    settings = Settings(_env_file=None)

    assert settings.database_url == "sqlite:///test.db"
