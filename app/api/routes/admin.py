from app.core.roles import Role
from app.dependencies.roles import require_role
from app.schemas.role import AdminResponseSchema
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/admin", response_model=AdminResponseSchema)
def admin_panel(user = Depends(require_role(Role.admin))):
    return AdminResponseSchema(ok=True)