CREATE TABLE IF NOT EXISTS routines (
  id INTEGER PRIMARY KEY,
  issue_id INTEGER,
  routine TEXT NOT NULL,
  created_at TEXT,
  FOREIGN KEY (issue_id) REFERENCES issues(id)
);