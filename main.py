from fastapi import FastAPI

from app.task_manager.database import Base, engine
from app.task_manager.routers.task import router
from app.task_manager.config import APP_NAME, APP_VERSION

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description="A simple Jira-like Task Management API built with FastAPI."
)

app.include_router(router)


@app.get("/", tags=["Health"])
def health_check():
    return {
        "status": "UP",
        "message": "Task Management Service is running successfully."
    }
