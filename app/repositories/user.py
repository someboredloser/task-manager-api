from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import UserORM

class UserRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, email: str, password: str) -> UserORM:
        user = UserORM(email=email, password=password)
        self.db.add(user)
        return user
    
    def get_by_email(self, email: str) -> UserORM:
        stmt = select(UserORM).where(UserORM.email==email)
        return self.db.scalars(stmt).first()