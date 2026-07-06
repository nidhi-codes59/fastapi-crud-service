from datetime import datetime, timezone

from app.common.config.db_manager import to_object_id
from app.common.constants.db_table_constants import COLLECTIONS


async def create_task_log(execute, task_obj, user_data, task_log_action, created_at=None, details={}):
    task_log_data = {
        "org_id": to_object_id(task_obj['org_id']),
        "workspace_id": to_object_id(task_obj['workspace_id']),
        "project_id": to_object_id(task_obj['project_id']),
        "task_id": to_object_id(task_obj['_id']),
        "stage": task_obj['stage'],
        "action": task_log_action,
        "cycle": task_obj['cycle'],
        "created_at": created_at,
        "created_by": to_object_id(user_data['_id']),
        "details": details
    }
    result = await execute.insert(COLLECTIONS.TASK_LOGS, task_log_data, return_document=True)
    return result


async def to_datetime(str_datetime):
    if isinstance(str_datetime, str):
        dt = datetime.fromisoformat(str_datetime).replace(tzinfo=timezone.utc) if str_datetime else 0
    else:
        return str_datetime
    return dt

from typing import Optional
from app.common.config.db_manager import Db_Ops_manager, to_object_id
from app.common.constants.db_table_constants import COLLECTIONS


async def get_project_template_type(db, project_id: str) -> Optional[str]:
    """
    Fetch template_type for a given project_id.
    Returns None if project not found.
    """
    execute = Db_Ops_manager(db)
    project = await execute.fetch_one(
        collection_name=COLLECTIONS.PROJECTS,
        condition={
            "_id":       to_object_id(project_id),
            "is_active": {"$in": [1, 2, 3]},
        },
        projection={"template_type": 1}
    )
    return project.get("template_type") if project else None
