from enum import Enum


class TaskStatus(Enum):
    CREATED = "created"
    QUEUED = "queued"
    UNDER_ANNOTATION = "under_annotation"
    ANNOTATED = "annotated"
    UNDER_REVIEW = "under_review"
    COMPLETED = "completed"
    REJECTED = "rejected"


class TaskPriority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class TaskStage(Enum):
    ANNOTATOR = "annotator"
    REVIEWER = "reviewer"


class TaskLogAction(Enum):
    ASSIGNED_TO_ANNOTATOR = "assigned_to_annotator"
    ASSIGNED_TO_REVIEWER = "assigned_to_reviewer"
    SKIPPED_BY_ANNOTATOR = "skipped_by_annotator"
    COMPLETED_BY_ANNOTATOR = "annotated"
    REVIEWED_BY_REVIEWER = "reviewed_by_reviewer"
    CREATED = "created"
    UPDATED = "updated"
    STATUS_CHANGED = "status_changed"
    ASSIGNED = "assigned"
    UNASSIGNED = "unassigned"
