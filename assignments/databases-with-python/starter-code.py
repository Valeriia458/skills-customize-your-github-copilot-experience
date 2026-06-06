import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

DATABASE_FILE = "assignments/databases-with-python/data.db"

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str
    price: float


def get_db_connection():
    connection = sqlite3.connect(DATABASE_FILE)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    with get_db_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                price REAL NOT NULL
            )
            """
        )
        conn.commit()


@app.on_event("startup")
def startup_event():
    initialize_database()


@app.get("/items")
def list_items():
    with get_db_connection() as conn:
        rows = conn.execute("SELECT id, name, description, price FROM items").fetchall()
        return [dict(row) for row in rows]


@app.post("/items")
def create_item(item: Item):
    with get_db_connection() as conn:
        cursor = conn.execute(
            "INSERT INTO items (name, description, price) VALUES (?, ?, ?)",
            (item.name, item.description, item.price),
        )
        conn.commit()
        item_id = cursor.lastrowid

        created_item = conn.execute(
            "SELECT id, name, description, price FROM items WHERE id = ?", (item_id,)
        ).fetchone()

        if created_item is None:
            raise HTTPException(status_code=500, detail="Failed to create item")

        return dict(created_item)
