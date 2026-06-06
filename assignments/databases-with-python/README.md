# 📘 Assignment: Databases with Python

## 🎯 Objective

Build a Python application that stores and retrieves structured data from a SQLite database, then connect it to API endpoints for persistent data access.

## 📝 Tasks

### 🛠️ Set up the database and data model

#### Description

Create a SQLite database and define a table to store items. Use Python to connect to the database, run schema setup, and perform basic insert and read operations.

#### Requirements
Completed program should:

- Create a SQLite database file if it does not already exist.
- Define a table schema for a simple entity such as `items`, `tasks`, or `products`.
- Insert at least one record into the database.
- Query the database and print results in a readable format.

### 🛠️ Add API endpoints backed by the database

#### Description

Build a small FastAPI app that uses the SQLite database for persistence. The API should allow clients to add new records and retrieve stored records.

#### Requirements
Completed program should:

- Use FastAPI to define at least one GET endpoint and one POST endpoint.
- Read data from the SQLite database in a GET endpoint and return it as JSON.
- Insert new data into the database using a POST endpoint.
- Use Pydantic models to validate incoming JSON request data.
- Return appropriate status codes and clear JSON responses.
