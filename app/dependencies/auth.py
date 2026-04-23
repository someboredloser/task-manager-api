from http.client import HTTPException

from fastapi import Depends, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.security import decode_token
from app.dependencies.db import get_db
from app.models.user import UserORM

ouath2 = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(
    token: str = Depends(ouath2),
    db: Session = Depends(get_db)
):
    payload = decode_token(token=token)
    
    if not payload: 
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    
    user_id = payload.get("sub")
    
    user = db.get(UserORM, user_id)
    
    if not user: 
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    
    return user