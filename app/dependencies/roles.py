from fastapi import Depends, HTTPException, status

from app.core.roles import Role
from app.dependencies.auth import get_current_user
from app.models.user import UserORM


def require_role(required_role: Role):
    def wrapper(user: UserORM = Depends(get_current_user)):
        if user.role != required_role.value:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
        return user
    return wrapper