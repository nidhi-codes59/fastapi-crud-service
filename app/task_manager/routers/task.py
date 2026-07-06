from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.task_manager.database import get_db
from app.task_manager.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from app.task_manager.services.task_service import TaskService

router = APIRouter(prefix="/tasks", tags=["Tasks"])

VALID_STATUS = ["To Do", "In Progress", "Done"]
VALID_PRIORITY = ["Low", "Medium", "High"]


@router.post("", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    if task.priority not in VALID_PRIORITY:
        raise HTTPException(status_code=400, detail="Invalid priority")
    return TaskService.create_task(db, task)


@router.get("", response_model=list[TaskResponse])
def get_all_tasks(db: Session = Depends(get_db)):
    return TaskService.get_all_tasks(db)


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = TaskService.get_task_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    if task.status and task.status not in VALID_STATUS:
        raise HTTPException(status_code=400, detail="Invalid status")
    if task.priority and task.priority not in VALID_PRIORITY:
        raise HTTPException(status_code=400, detail="Invalid priority")

    updated = TaskService.update_task(db, task_id, task)
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated


@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    deleted = TaskService.delete_task(db, task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}
