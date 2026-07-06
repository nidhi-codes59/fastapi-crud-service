from app.common.config.db_manager import to_object_id
from app.common.constants.db_table_constants import COLLECTIONS
from app.common.constants.rbac.rbac_constants import USER_ROLES_CONSTANTS


class TaskPermission:

    def __init__(self, execute, loggedin_user_data, log):
        self.execute = execute
        self.loggedin_user_data = loggedin_user_data
        self.log = log
        self.allowed_roles = []

    async def has_permission_to_create_task(self, project_id: str) -> bool:
        if self.loggedin_user_data.get("role") == USER_ROLES_CONSTANTS.super_admin:
            return True

        self.allowed_roles = [
            USER_ROLES_CONSTANTS.org_admin,
            USER_ROLES_CONSTANTS.workspace_manager,
            USER_ROLES_CONSTANTS.project_manager,
        ]

        project_obj = await self.execute.fetch_one(
            COLLECTIONS.PROJECTS,
            condition={
                "_id": to_object_id(project_id)
            }
        )

        if not project_obj:
            return False

        assignments = self.loggedin_user_data.get("assignments")

        self.log.debug(f"User assignments: {assignments}")

        if await self._has_permission(assignments, "project", project_obj['_id']):
            return True

        # Check role at workspace-level
        if await self._has_permission(assignments, "workspace", project_obj['workspace_id']):
            return True

        # Check role at organization-level
        if await self._has_permission(assignments, "organization", project_obj['org_id']):
            return True

        return False

    async def _has_permission(self, assignments, entity_type, entity_id):
        for a in assignments:
            if (
                    a["entity"] == entity_type
                    and a["entity_id"] == to_object_id(entity_id)
                    and a["role_id"] in self.allowed_roles
            ):
                return True
        return False

    async def has_permission_to_annotate_task(self, project_id: str) -> bool:
        if self.loggedin_user_data.get("role") == USER_ROLES_CONSTANTS.super_admin:
            return True

        self.allowed_roles = [
            USER_ROLES_CONSTANTS.annotator,
            # USER_ROLES_CONSTANTS.org_admin,
            # USER_ROLES_CONSTANTS.workspace_manager,
            # USER_ROLES_CONSTANTS.project_manager,
        ]

        project_obj = await self._get_project_obj(project_id=project_id)

        if not project_obj:
            return False

        assignments = self.loggedin_user_data.get("assignments")

        self.log.debug(f"User assignments: {assignments}")

        if await self._has_permission(assignments, "project", project_obj['_id']):
            return True

        return False
    
    async def _get_project_obj(self, project_id):
        project_obj = await self.execute.fetch_one(
            COLLECTIONS.PROJECTS,
            condition={
                "_id": to_object_id(project_id)
            }
        )
        return project_obj
    
    async def has_permission_to_fetch_all_tasks(self, project_id: str):
        if self.loggedin_user_data.get("role") == USER_ROLES_CONSTANTS.super_admin:
            return True
        self.allowed_roles = [
            USER_ROLES_CONSTANTS.org_admin,
            USER_ROLES_CONSTANTS.workspace_manager,
            USER_ROLES_CONSTANTS.project_manager,
        ]

        project_obj = await self._get_project_obj(project_id)
        if not project_obj:
            return False
        
        assignments = self.loggedin_user_data.get("assignments")

        self.log.debug(f"User assignments: {assignments}")

        if await self._has_permission(assignments, "project", project_obj['_id']):
            return True

        # Check role at workspace-level
        if await self._has_permission(assignments, "workspace", project_obj['workspace_id']):
            return True

        # Check role at organization-level
        if await self._has_permission(assignments, "organization", project_obj['org_id']):
            return True

        return False
    
    async def has_permission_to_review_tasks(self, project_id: str):
        if self.loggedin_user_data.get("role") == USER_ROLES_CONSTANTS.super_admin:
            return True
        self.allowed_roles = [
            USER_ROLES_CONSTANTS.reviewer,
        ]

        project_obj = await self._get_project_obj(project_id)
        if not project_obj:
            return False
        
        assignments = self.loggedin_user_data.get("assignments")

        self.log.debug(f"User assignments: {assignments}")

        if await self._has_permission(assignments, "project", project_obj['_id']):
            return True

        return False
    
    async def has_permission_to_view_task_details(self, project_id: str):
        if self.loggedin_user_data.get("role") == USER_ROLES_CONSTANTS.super_admin:
            return True
        self.allowed_roles = [
            USER_ROLES_CONSTANTS.org_admin,
            USER_ROLES_CONSTANTS.workspace_manager,
            USER_ROLES_CONSTANTS.project_manager
        ]

        project_obj = await self._get_project_obj(project_id)
        if not project_obj:
            return False
        
        assignments = self.loggedin_user_data.get("assignments")

        self.log.debug(f"User assignments: {assignments}")

        if await self._has_permission(assignments, "project", project_obj['_id']):
            return True

        # Check role at workspace-level
        if await self._has_permission(assignments, "workspace", project_obj['workspace_id']):
            return True

        # Check role at organization-level
        if await self._has_permission(assignments, "organization", project_obj['org_id']):
            return True

        return False
    
        

        

