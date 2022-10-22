from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    db_connection_string: PostgresDsn = (
        "postgresql://sosaedison@localhost/fast-api-chat"
    )
