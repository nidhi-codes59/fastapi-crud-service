from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.task_manager.database import Base

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String(500), nullable=True)
    status = Column(
        String(20),
        nullable=False,
        default="To Do"
    )
    priority = Column(
        String(20),
        nullable=False,
        default="Medium"
    )
    assignee = Column(
        String(100),
        nullable=True
    )
    due_date = Column(
        String(20),
        nullable=True
    )
    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )