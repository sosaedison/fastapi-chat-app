from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import Settings, DevSettings

settings = DevSettings()
if not settings.dev:
    settings = Settings()

engine = create_engine(settings.db_connection_string)
SessionLocal = sessionmaker(autocommit=True, autoflush=True, bind=engine)

Base = declarative_base()
