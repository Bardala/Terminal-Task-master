import sqlite3
import os


class SqlDataStore:
    def __init__(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(script_dir, "./data_store.db")
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self.c = self.conn.cursor()
        self._migrate()

    def _migrate(self):
        """Run all the migration sql files in the migrations directory."""
        migration_dir = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "migrations"
        )
        for filename in os.listdir(migration_dir):
            if filename.endswith(".sql"):
                with open(os.path.join(migration_dir, filename), "r") as f:
                    sql_command = f.read()
                self.c.execute(sql_command)
                self.conn.commit()

    def add_project(self, name, directory):
        sql = "INSERT INTO projects (name, directory) VALUES (?, ?)"
        self.c.execute(sql, (name, directory))
        self.conn.commit()

    def get_project_by_name(self, name):
        sql = "SELECT * FROM projects WHERE name=?"
        self.c.execute(sql, (name,))
        return self.c.fetchone()

    def get_all_projects(self):
        sql = "SELECT * FROM projects"
        self.c.execute(sql)
        return self.c.fetchall()

    def delete_project_by_name(self, name):
        sql = "DELETE FROM projects WHERE name=?"
        self.c.execute(sql, (name,))
        self.conn.commit()

    def update_project_by_name(self, name, new_directory):
        sql = "UPDATE projects SET directory=? WHERE name=?"
        self.c.execute(sql, (new_directory, name))
        self.conn.commit()

    def _drop_table_todos(self):
        self.c.execute("DROP TABLE IF EXISTS todos")
        self.conn.commit()

    def add_todo(self, todo):
        sql = "INSERT INTO todos (id, task, due_date, status, created_at) VALUES (?, ?, ?, ?, ?)"
        self.c.execute(
            sql,
            (
                todo["id"],
                todo["task"],
                todo["due_date"],
                todo["status"],
                todo["created_at"],
            ),
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
        self.conn.commit()

    def get_last_todo_id(self):
        self.c.execute("SELECT id FROM todos ORDER BY id DESC LIMIT 1")
        last_id = self.c.fetchone()
        return last_id[0] if last_id else 0

    def update_todo_by_id(self, id, new_task):
        sql = "UPDATE todos SET task=? WHERE id=?"
        todo = self.c.execute(sql, (new_task, id))
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
