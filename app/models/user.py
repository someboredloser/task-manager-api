from app.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column

class UserORM(Base):
    __tablename__ = "users"
    
    email: Mapped[str] = mapped_column(unique=True, index=True)
    password: Mapped[str] = mapped_column()
    