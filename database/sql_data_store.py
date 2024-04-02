import sqlite3


class SqlDataStore:
    def __init__(self):
        self.conn = sqlite3.connect("./data_store.db")
        self.conn.row_factory = sqlite3.Row
        self.c = self.conn.cursor()
        self._create_table_todos()

    def _create_table_todos(self):
        self.c.execute(
            """
            CREATE TABLE IF NOT EXISTS todos (
                id INTEGER PRIMARY KEY,
                task TEXT NOT NULL,
                due_date TEXT,
                status BOOLEAN NOT NULL,
                created_at TEXT
            )
            """
        )
        self.conn.commit()

    def _drop_table_todos(self):
        self.c.execute("DROP TABLE IF EXISTS todos")
        self.conn.commit()

    def add_todo(self, todo):
        self.c.execute(
            "INSERT INTO todos (id, task, due_date, status, created_at) VALUES (?, ?, ?, ?, ?)",
            (todo["id"], todo["task"], todo["due_date"], todo["status"], todo["created_at"]),
        )
        self.conn.commit()

    def get_all_todos(self):
        self.c.execute("SELECT * FROM todos")
        return self.c.fetchall()

    def get_todo_by_id(self, id):
        self.c.execute("SELECT * FROM todos WHERE id=?", (id,))
        return self.c.fetchone()

    def toggle_todo(self, id):
        self.c.execute("SELECT status FROM todos WHERE id=?", (id,))
        status = self.c.fetchone()[0]
        # status type in db in boolean
        status = not status
        self.c.execute("UPDATE todos SET status=? WHERE id=?", (status, id))

    def update_todo_by_id(self, id, new_task):
        todo = self.c.execute("UPDATE todos SET task=? WHERE id=?", new_task, id)
        self.conn.commit()
        print(f"todo from sql method: {todo}")

    def delete_todo_by_id(self, id):
        self.c.execute("DELETE FROM todos WHERE id=?", (id,))
        self.conn.commit()

    def delete_all_todos(self):
        self.c.execute("DELETE FROM todos")
        self.conn.commit()

    def close(self):
        self.conn.close()
