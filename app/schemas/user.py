from pydantic import BaseModel, ConfigDict


class UserSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: str
    email: str
    
class CreateUserSchema(BaseModel):
    email: str
    password:str
    
class LoginSchema(BaseModel):
    email: str
    password: str
    
class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"