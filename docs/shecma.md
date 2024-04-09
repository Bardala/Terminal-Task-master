# Database Schema

- [Table: todos](#table-todos)
- [Table: projects](#table-projects)
- [Table: issues](#table-issues)
- [Table: routines](#table-routines)


## Table: todos

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| id          | INTEGER   | Primary key |
| task        | TEXT      | Not null    |
| due_date    | TEXT      |             |
| status      | BOOLEAN   | Not null    |
| created_at  | TEXT      |             |

---

## Table: projects

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| id          | INTEGER   | Primary key |
| name        | TEXT      | Not null, unique |
| directory   | TEXT      | Not null, unique |

---

## Table: issues

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| id          | INTEGER   | Primary key |
| issue       | TEXT      | Not null    |
| created_at  | TEXT      |             |

---

## Table: routines

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| id          | INTEGER   | Primary key |
| issue_id    | INTEGER   | Foreign key referencing issues(id) |
| routine     | TEXT      | Not null    |
| created_at  | TEXT      |             |