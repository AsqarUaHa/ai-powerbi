import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from .base import Base


DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError(
        "DATABASE_URL environment variable is not set. "
        "Expected PostgreSQL URL, e.g. postgresql+psycopg2://user:pass@host:port/dbname",
    )


engine = create_engine(DATABASE_URL, future=True)
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    class_=Session,
)


def get_db() -> Session:
    """Зависимость FastAPI для получения DB-сессии.

    Использование в роутере:

        from fastapi import Depends
        from sqlalchemy.orm import Session
        from ..db.session import get_db

        def endpoint(db: Session = Depends(get_db)):
            ...
    """

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
