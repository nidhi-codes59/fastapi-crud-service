from sqlalchemy.orm import Session

from app.task_manager.models.task import Task
from app.task_manager.schemas.task import TaskCreate, TaskUpdate


class TaskService:

    @staticmethod
    def create_task(db: Session, task: TaskCreate):
        new_task = Task(
            title=task.title,
            description=task.description,
            priority=task.priority,
            assignee=task.assignee,
            due_date=task.due_date
        )
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        return new_task

    @staticmethod
    def get_all_tasks(db: Session):
        return db.query(Task).all()

    @staticmethod
    def get_task_by_id(db: Session, task_id: int):
        return db.query(Task).filter(Task.id == task_id).first()

    @staticmethod
    def update_task(db: Session, task_id: int, task: TaskUpdate):
        existing_task = db.query(Task).filter(Task.id == task_id).first()
        if not existing_task:
            return None

        update_data = task.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(existing_task, key, value)

        db.commit()
        db.refresh(existing_task)
        return existing_task

    @staticmethod
    def delete_task(db: Session, task_id: int):
        existing_task = db.query(Task).filter(Task.id == task_id).first()
        if not existing_task:
            return None

        db.delete(existing_task)
        db.commit()
        return existing_task
