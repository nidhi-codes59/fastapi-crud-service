"""
Application configuration and constants.
"""

DATABASE_URL = "sqlite:///./task_manager.db"

TASK_STATUS = [
    "To Do",
    "In Progress",
    "Done"
]

TASK_PRIORITY = [
    "Low",
    "Medium",
    "High"
]

APP_NAME = "Task Management Service"
APP_VERSION = "1.0.0"
