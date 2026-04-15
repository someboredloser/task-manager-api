from sqlalchemy.orm import sessionmaker
from app.database import engine


SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine,
)
