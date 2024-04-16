from datetime import datetime
import sqlite3
import os
from typing import List, Dict, Union


# Todo: create a mock_db for testing
class SqlDataStore:
    def __init__(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(script_dir, "./data_store.db")
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self.c = self.conn.cursor()
        self._migrate()

    def _migrate(self) -> None:
        """Run all the migration sql files in the migrations directory."""
        migration_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "migrations")
        for filename in os.listdir(migration_dir):
            if filename.endswith(".sql"):
                with open(os.path.join(migration_dir, filename), "r") as f:
                    sql_command = f.read()
                self.c.execute(sql_command)
                self.conn.commit()

    def add_project(self, name: str, directory: str) -> None:
        sql = "INSERT INTO projects (name, directory) VALUES (?, ?)"
        self.c.execute(sql, (name, directory))
        self.conn.commit()

    def get_project_by_name(self, name: str) -> Union[sqlite3.Row, None]:
        sql = "SELECT * FROM projects WHERE name=?"
        self.c.execute(sql, (name,))
        return self.c.fetchone()

    def get_all_projects(self) -> List[sqlite3.Row]:
        sql = "SELECT * FROM projects"
        self.c.execute(sql)
        return self.c.fetchall()

    def delete_project_by_name(self, name: str) -> None:
        sql = "DELETE FROM projects WHERE name=?"
        self.c.execute(sql, (name,))
        self.conn.commit()

    def update_project_by_name(self, name: str, new_directory: str) -> None:
        sql = "UPDATE projects SET directory=? WHERE name=?"
        self.c.execute(sql, (new_directory, name))
        self.conn.commit()

    def add_todo(self, todo: Dict[str, Union[int, str, bool, datetime]]) -> None:
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

    def get_all_todos(self) -> List[sqlite3.Row]:
        self.c.execute("SELECT * FROM todos")
        return self.c.fetchall()

    def get_todo_by_id(self, id: int) -> Union[sqlite3.Row, None]:
        self.c.execute("SELECT * FROM todos WHERE id=?", (id,))
        return self.c.fetchone()

    def toggle_todo(self, id: int) -> None:
        self.c.execute("SELECT status FROM todos WHERE id=?", (id,))
        status = self.c.fetchone()[0]
        # status type in db in boolean
        status = not status
        self.c.execute("UPDATE todos SET status=? WHERE id=?", (status, id))
        self.conn.commit()

    def get_last_todo_id(self) -> int:
        self.c.execute("SELECT id FROM todos ORDER BY id DESC LIMIT 1")
        last_id = self.c.fetchone()
        return last_id[0] if last_id else 0

    def update_todo_by_id(self, id: int, new_task: str) -> None:
        sql = "UPDATE todos SET task=? WHERE id=?"
        todo = self.c.execute(sql, (new_task, id))
        self.conn.commit()
        print(f"todo from sql method: {todo}")

    def delete_todo_by_id(self, id: int) -> None:
        self.c.execute("DELETE FROM todos WHERE id=?", (id,))
        self.conn.commit()

    def delete_all_todos(self) -> None:
        self.c.execute("DELETE FROM todos")
        self.conn.commit()

    def add_issue(self, issue: str) -> None:
        created_at = datetime.now()
        sql = "INSERT INTO issues (issue, created_at) VALUES (?, ?)"
        self.c.execute(sql, (issue, created_at))
        self.conn.commit()

    def get_issue_by_name(self, issue_name: str) -> Union[sqlite3.Row, None]:
        self.c.execute("SELECT * FROM issues WHERE issue=?", (issue_name,))
        return self.c.fetchone()

    def get_issues(self) -> List[sqlite3.Row]:
        self.c.execute("SELECT * FROM issues")
        return self.c.fetchall()

    def update_issue(self, id: int, new_issue: str) -> None:
        sql = "UPDATE issues SET issue=? WHERE id=?"
        self.c.execute(sql, (new_issue, id))
        self.conn.commit()

    def delete_issue(self, id: int) -> None:
        self.c.execute("DELETE FROM issues WHERE id=?", (id,))
        self.conn.commit()

    def add_issue_routine(self, issue_routine: Dict[str, Union[int, str]]) -> None:
        sql = "INSERT INTO routines (issue_id, routine) VALUES (?, ?)"
        self.c.execute(sql, (issue_routine["issue_id"], issue_routine["routine"]))
        self.conn.commit()

    def get_issue_routines(self, issue_id: int) -> List[sqlite3.Row]:
        self.c.execute("SELECT * FROM routines WHERE issue_id=?", (issue_id,))
        return self.c.fetchall()

    def close(self) -> None:
        self.conn.close()
