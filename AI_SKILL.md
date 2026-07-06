# AI Skill: API Documentation Generation

## Objective
This AI skill automatically generates clear and structured API documentation from the FastAPI application. It helps developers understand available endpoints, request parameters, response models, and error responses without manually writing documentation.

## Problem Statement
Maintaining API documentation manually can be time-consuming and error-prone. As APIs evolve, documentation often becomes outdated.

An AI-powered documentation assistant can analyze the FastAPI project and generate accurate, up-to-date documentation automatically.


## Input
The AI analyzes the following project files:

- FastAPI route definitions
- Request schemas (Pydantic)
- Response schemas (Pydantic)
- HTTP methods
- Endpoint paths

Example Input:

```python
@router.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate):
    ...
```

## AI Workflow

1. Scan the FastAPI project.
2. Identify all API routes.
3. Read the HTTP method for each endpoint.
4. Extract the endpoint path.
5. Read the request and response schemas.
6. Detect possible HTTP status codes.
7. Generate structured API documentation in Markdown or HTML format.

## Example

### Input
```python
@router.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    ...
```

### AI Generated Documentation

Endpoint
GET /tasks/{task_id}

Description
Retrieves a task using its unique ID.

Request Parameter
| Name | Type | Required |
|------|------|----------|
| task_id | Integer | Yes |

Response
```json
{
  "id": 1,
  "title": "Build FastAPI Project",
  "status": "To Do",
  "priority": "High"
}
```

**Possible Status Codes**
- 200 – Success
- 404 – Task Not Found


## Expected Output
The AI generates documentation containing:
- Endpoint URL
- HTTP Method
- Description
- Request Parameters
- Request Body
- Response Body
- HTTP Status Codes
- Example Requests
- Example Responses


## Benefits
- Reduces manual documentation effort.
- Keeps documentation synchronized with the source code.
- Improves developer productivity.
- Makes APIs easier to understand.
- Helps frontend and backend teams collaborate effectively.


## Conclusion
The AI-powered API Documentation Skill simplifies the process of maintaining API documentation by automatically analyzing FastAPI routes and generating clear, structured, and up-to-date documentation. This improves developer experience while reducing maintenance effort.
