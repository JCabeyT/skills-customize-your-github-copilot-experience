# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to create a simple RESTful web service using the FastAPI framework in Python. You will define endpoints, handle requests, and return JSON responses.

## 📝 Tasks

### 🛠️ Task 1: Setup and basic endpoints

#### Description
Install FastAPI (and uvicorn) and create a new Python file that initializes a FastAPI application. Define at least two `GET` endpoints: one that returns a welcome message and another that echoes a path parameter.

#### Requirements
Completed program should:

- Import and instantiate `FastAPI` in a Python script
- Use `@app.get` decorators to create endpoints
- Return JSON responses from each endpoint
- Be able to run with `uvicorn` and respond to requests at `http://localhost:8000`

### 🛠️ Task 2: CRUD-style operations

#### Description
Expand the application with additional routes to simulate creating, reading, updating, and deleting resources (in-memory). Use request bodies and path/query parameters.

#### Requirements
Completed program should:

- Define `POST`, `PUT`, and `DELETE` endpoints with appropriate paths
- Use Pydantic models for request bodies
- Manage a simple in-memory list or dictionary to store items
- Return appropriate status codes and messages


**Skills practiced:** Web frameworks, REST API design, decorators, JSON handling, and basic server setup