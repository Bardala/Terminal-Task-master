import sqlite3


class SqlDataStore:
    def __init__(self):
        self.conn = sqlite3.connect("data_store.db")
        self.c = self.conn.cursor()

    def run(self):
        self._create_table_todos()

    def _create_table_todos(self):
        self.c.execute(
            """
            CREATE TABLE IF NOT EXISTS todos (
                id INTEGER PRIMARY KEY,
                task TEXT NOT NULL,
                due_date TEXT NOT NULL,
                status BOOLEAN NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )
        self.conn.commit()

    def add_todo(self, todo):
        self.c.execute(
            "INSERT INTO todos (id, task, due_date, status, created_at) VALUES (?, ?, ?, ?)",
            todo.id,
            todo.task,
            todo.due_date,
            todo.status,
            todo.created_at,
        )
        self.conn.commit()

    def get_all_todos(self):
        self.c.execute("SELECT * FROM todos")
        return self.c.fetchall()

    def get_todo_by_id(self, id):
        self.c.execute("SELECT * FROM todos WHERE id=?", id)
        return self.c.fetchone()

    def toggle_todo(self, id):
        self.c.execute("SELECT status FROM todos WHERE id=?", id)
        status = self.c.fetchone()[0]
        # status type in db in boolean
        status = not status
        self.c.execute("UPDATE todos SET status=? WHERE id=?", status, id)

    def delete_todo_by_id(self, id):
        self.c.execute("DELETE FROM todos WHERE id=?", id)
        self.conn.commit()

    def close(self):
        self.conn.close()
