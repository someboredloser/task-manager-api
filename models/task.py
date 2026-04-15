from uuid import uuid4

from app.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column

class User(Base):
    id: Mapped[str] = mapped_column(primary_key=True, default=lambda: str(uuid4()))