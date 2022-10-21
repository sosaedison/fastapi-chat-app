from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL: str = f"postgresql://{os.environ.get('POSTGRESS_USERNAME')}:{os.environ.get('POSTGRESS_PASSWORD')}@postgresserver/fast-api-chat"
SQLALCHEMY_DATABASE_URL: str = f"postgresql://sosaedison@localhost/fast-api-chat"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
Base.metadata.schema = "local"


# from contextlib import contextmanager
# from sqlalchemy import create_engine
# from sqlalchemy.orm.session import sessionmaker


# class Database:
#     """Connects to the database and provides a session scope for safe db transactions"""

#     def __init__(self, app):
#         """Set class up with db config from app config"""
#         self.db_uri = app.config["DB_URI"]
#         self.db_kwargs = {}
#         self.db_kwargs["echo"] = app.config["DB_ECHO"]
#         self.db_kwargs["echo_pool"] = app.config["DB_ECHO_POOL"]

#         self.init_engine()

#     def init_engine(self):
#         """Create the engine and session"""
#         self.engine = create_engine(self.db_uri, **self.db_kwargs)
#         self.Session = sessionmaker(bind=self.engine)  # pylint: disable=invalid-name

#     # pylint: disable=no-self-use
#     def create_db(self, app):
#         """Drop all existing tables and create new ones according to ORM mapping in models.py"""
#         # pylint: disable=no-member
#         # Base.metadata.drop_all(app.db.engine)
#         # Base.metadata.create_all(app.db.engine)

#     @contextmanager
#     def session_scope(self):
#         """Provide a transactional scope around a series of operations."""
#         session = self.Session()
#         try:
#             yield session
#             session.commit()
#         except:
#             session.rollback()
#             raise
#         finally:
#             session.close()
