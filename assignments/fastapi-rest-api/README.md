# 📘 Assignment: FastAPI REST API

## 🎯 Objective

Build a simple REST API using the FastAPI framework to practice endpoint design, request handling, and JSON responses.

## 📝 Tasks

### 🛠️ Define API Endpoints and Request Handling

#### Description

Create API routes using FastAPI that respond to HTTP GET and POST requests with JSON data.

#### Requirements
Completed program should:

- Use FastAPI to define at least one GET endpoint and one POST endpoint.
- Return JSON responses from each endpoint.
- Accept path or query parameters in a GET request.
- Accept JSON input in a POST request and include the submitted data in the response.

### 🛠️ Add Data Validation and Response Structure

#### Description

Use Pydantic models to validate incoming request data and return structured JSON responses.

#### Requirements
Completed program should:

- Define a Pydantic model for request data.
- Validate the JSON body in the POST request.
- Return a clear response object with the submitted data and any additional metadata.
- Use appropriate HTTP status codes for success responses.
