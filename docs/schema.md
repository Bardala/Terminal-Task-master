# Database Schema

[Table: todos](#table-todos) | id | task | due_date | status | created_at|
  --- | --- | --- | --- | --- | ---

[Table: projects](#table-projects) | id | name | directory |
  --- | --- | --- | ---

[Table: folders](#table-folders) | id | name |
  --- | --- | ---

[Table: item_folders](#table-item_folders) | item_id | folder_id |
  --- | --- | --- 
  
[Table: issues](#table-issues) | id | issue | created_at |
  --- | --- | --- | ---
  
[Table: routines](#table-routines) | id | issue_id | routine | created_at |
  --- | --- | --- | --- | ---
  




## Table: todos

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| id          | INTEGER   | Primary key |
| task        | TEXT      | Not null    |
| due_date    | TEXT      |             |
| status      | BOOLEAN   | Not null    |
| created_at  | TEXT      |             |


## Table: projects

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| id          | INTEGER   | Primary key |
| name        | TEXT      | Not null, unique |
| directory   | TEXT      | Not null, unique |


## Table: folders

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| id          | INTEGER   | Primary key |
| name        | TEXT      | Not null, unique |

## Table: item_folders

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| item_id  | INTEGER   | Foreign key referencing `projects(id)` |
| folder_id   | INTEGER   | Foreign key referencing `folders(id)` |
| PRIMARY KEY | (`project_id`, `folder_id`) | Composite primary key |

## Table: issues

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| id          | INTEGER   | Primary key |
| issue       | TEXT      | Not null    |
| created_at  | TEXT      |             |


## Table: routines

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| id          | INTEGER   | Primary key |
| issue_id    | INTEGER   | Foreign key referencing `issues(id)` |
| routine     | TEXT      | Not null    |
| created_at  | TEXT      |             |