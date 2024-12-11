import sqlite3
from contextlib import contextmanager
import os

DATABASE_PATH = os.path.join(os.path.dirname(__file__), "../../data/metadata.db")


def init_db():
    data_dir = os.path.dirname(DATABASE_PATH)
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        print(f"Created directory: {data_dir}")

    if not os.path.exists(DATABASE_PATH):
        with sqlite3.connect(DATABASE_PATH) as conn:
            print(f"Created database: {DATABASE_PATH}")

    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS queues (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                type INTEGER NOT NULL,
                ttl_seconds INTEGER NOT NULL,
                max_size INTEGER NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
        """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            queue_id INTEGER NOT NULL,
            content TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(queue_id) REFERENCES queues(id)
            );
        """
        )
        conn.commit()


@contextmanager
def get_db_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()


def execute_query(query, params=None):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, params or ())
        conn.commit()
        return cursor


def fetch_all(query, params=None):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, params or ())
        return cursor.fetchall()


def fetch_one(query, params=None):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, params or ())
        return cursor.fetchone()
