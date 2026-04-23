from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.task import router as task_router
from app.api.routes.auth import router as auth_router
from app.core.config import settings


app = FastAPI(
    title="TASK-MANAGER",
    debug=settings.debug
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(task_router)
app.include_router(auth_router)
