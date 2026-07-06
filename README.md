# Task Management Service

## Overview
Task Management Service is a RESTful API built using FastAPI. It allows users to manage tasks by creating, viewing, updating, and deleting them. The project follows a layered architecture to keep the code organized and maintainable.

## Features
- Create a new task
- Retrieve all tasks
- Retrieve a task by ID
- Update an existing task
- Delete a task
- Request validation using Pydantic
- Database operations using SQLAlchemy
- Logging support
- Unit testing using Pytest
- CI pipeline using GitHub Actions
- Docker support

## Technology Stack
- Python 3.11
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Pytest
- GitHub Actions
- Docker

## Installation
Clone the repository:
git clone <repository-url>
cd task-manager

Install the dependencies:
pip install -r requirements.txt

## Run the Application
Start the FastAPI server:
uvicorn main:app --reload

The application will be available at:
http://127.0.0.1:8000

Swagger API documentation
http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /tasks | Create a task |
| GET | /tasks | Retrieve all tasks |
| GET | /tasks/{id} | Retrieve a task by ID |
| PUT | /tasks/{id} | Update a task |
| DELETE | /tasks/{id} | Delete a task |

## Running Tests
Execute the unit tests using:
pytest

## Docker
Build the Docker image:
docker build -t task-manager .

Run the Docker container:
docker run -p 8000:8000 task-manager

## Continuous Integration
A GitHub Actions workflow is included to:
- Install project dependencies
- Run unit tests
- Verify that the FastAPI application starts successfully