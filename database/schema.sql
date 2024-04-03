CREATE TABLE IF NOT EXISTS todos (
    id INTEGER PRIMARY KEY,
    task TEXT NOT NULL,
    due_date TEXT,
    status BOOLEAN NOT NULL,
    created_at TEXT
);