from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    dev = False
    db_connection_string: str = (
        "postgresql://sosaedison@docker.for.mac.host.internal:5432/fast-api-chat"
    )


class DevSettings(Settings):
    dev = True
    db_connection_string: str = "sqlite:///xchange.db"
