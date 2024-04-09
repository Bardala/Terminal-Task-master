CREATE TABLE IF NOT EXISTS todos (
    id INTEGER PRIMARY KEY,
    task TEXT NOT NULL,
    due_date TEXT,
    status BOOLEAN NOT NULL,
    created_at TEXT
);

CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    directory TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS routines (
    id INTEGER PRIMARY KEY,
    issue TEXT NOT NULL,
    suggested_routine TEXT NOT NULL,
);