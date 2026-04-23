from fastapi import APIRouter, Depends

from app.dependencies.auth import get_current_user
from app.dependencies.db import get_auth_service
from app.schemas.user import CreateUserSchema, LoginSchema, TokenSchema, UserSchema
from app.services.auth import AuthService


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserSchema)
def user_register(
    payload: CreateUserSchema, 
    service: AuthService = Depends(get_auth_service)
):
    return service.register(email=payload.email, password=payload.password)

@router.post("/login", response_model=TokenSchema)
def login(
    payload: LoginSchema,
    service: AuthService = Depends(get_auth_service)
):
    return service.login(payload.email, payload.password)

@router.get("/me", response_model=UserSchema)
def me(user=Depends(get_current_user)):
    return user
