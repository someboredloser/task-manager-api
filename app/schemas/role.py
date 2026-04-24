from pydantic import BaseModel


class AdminResponseSchema(BaseModel):
    ok: bool = False