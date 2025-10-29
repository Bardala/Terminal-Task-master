# Terminal Task Manager

A comprehensive command-line personal management tool built with Python that helps you organize todos, projects, moods, and Windows settings through an intuitive terminal interface.

## Features

### 🎯 Todo Management

- **Add todos**: Create new tasks with automatic ID assignment
- **List todos**: View all tasks with completion status (✅/❌)
- **Toggle status**: Mark tasks as complete/incomplete
- **Set done**: Force complete a task
- **Update tasks**: Modify existing todo items
- **Delete todos**: Remove individual tasks or clear all at once
- **Package operations**: Handle grouped tasks (tasks starting with "\_\_")

### 📁 Project Management

- **Add projects**: Register project names with their directories
- **Open in VSCode**: Quickly launch projects in Visual Studio Code
- **List projects**: View all registered projects
- **Update directories**: Modify project paths
- **Delete projects**: Remove project entries
- **CLI integration**: Access PowerShell, Command Prompt, and Bash directly
- **Folder organization**: Group projects into folders for better organization

### 😊 Mood Manager

- **Issue tracking**: Record common problems or moods (boredom, anxiety, etc.)
- **Routine suggestions**: Add recommended routines for specific issues
- **Mood-based help**: Get suggested routines when experiencing certain moods
- **Smart matching**: Automatically link routines to existing issues

### ⚙️ Windows Settings

- **Theme control**: Switch between light/dark mode for system and apps
- **Quick app access**: Open common Windows apps (Music, Edge, Store, Settings, etc.)
- **Web search**: Quick search on Google, Bing, YouTube
- **Productivity tools**: Access Calendar, Mail, Photos, Camera, Maps
- **Prayer times**: Quick access to Muslim prayer times

## Installation

### Prerequisites

- Python 3.7+
- Visual Studio Code (for project opening feature)
- Windows OS (for Windows settings features)

### Setup

1. Clone the repository:

```bash
git clone https://github.com/Bardala/Terminal-Task-master
cd terminal-task-manager
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python main.py
```

## Usage

### Main Interface

When you start the application, you'll see the main prompt:

```
bardala>
```

### Available Modes

#### Todo Mode (`todo`)

Manage your task list:

```
bardala> todo
todo> help
Available commands:
add, toggle, done, list, delete, update, delete_all, clear, help

todo> add
add new todo
>>> Complete project documentation
>>> Buy groceries
>>> /

todo> list
1. Complete project documentation - ❌
2. Buy groceries - ❌

todo> toggle 1
'Complete project documentation' is now completed

todo> list
1. Complete project documentation - ✅
2. Buy groceries - ❌
```

#### Project Mode (`project`)

Manage and open your coding projects:

```
bardala> project
project> add
Enter project name: my-app
Enter project dir: C:/Projects/my-app

project> list
my-app: C:/Projects/my-app

project> open my-app
# Opens the project in VSCode
```

#### Mood Mode (`mood`)

Manage routines for different emotional states:

```
bardala> mood
mood> add
>>> What is the issue?
>> boredom
>>> What is the routine?
>> Watch philosophical videos

mood> mood
>>> What is your mood?
1. boredom
>> boredom
- Watch philosophical videos
```

#### Settings Mode (`settings`)

Quick Windows utilities:

```
bardala> settings
settings> dark
Dark mode turned on

settings> light
Light mode turned on

settings> google
Enter search query: python tutorials
# Opens Google search in Edge

settings> youtube
Enter search query: music for coding
# Opens YouTube search
```

### Common Commands

- `help` - Show available commands for current mode
- `clear` - Clear the screen
- `/` - Exit current mode and return to main menu
- `//` - Exit the application entirely

## Database Schema

The application uses SQLite with the following tables:

### Todos Table

| Column     | Type    | Constraints | Description                                      |
| ---------- | ------- | ----------- | ------------------------------------------------ |
| id         | INTEGER | PRIMARY KEY | Unique identifier for each task                  |
| task       | TEXT    | NOT NULL    | The task description                             |
| due_date   | TEXT    |             | Optional due date for the task                   |
| status     | BOOLEAN | NOT NULL    | Completion status (0 = incomplete, 1 = complete) |
| created_at | TEXT    |             | Timestamp when the task was created              |

### Projects Table

| Column    | Type    | Constraints      | Description                               |
| --------- | ------- | ---------------- | ----------------------------------------- |
| id        | INTEGER | PRIMARY KEY      | Unique identifier for each project        |
| name      | TEXT    | NOT NULL, UNIQUE | Project name (must be unique)             |
| directory | TEXT    | NOT NULL, UNIQUE | File system path to the project directory |

### Issues Table

| Column     | Type    | Constraints      | Description                            |
| ---------- | ------- | ---------------- | -------------------------------------- |
| id         | INTEGER | PRIMARY KEY      | Unique identifier for each issue       |
| issue      | TEXT    | NOT NULL, UNIQUE | Problem or emotional state description |
| created_at | TEXT    |                  | Timestamp when the issue was recorded  |

### Routines Table

| Column     | Type    | Constraints                       | Description                            |
| ---------- | ------- | --------------------------------- | -------------------------------------- |
| id         | INTEGER | PRIMARY KEY                       | Unique identifier for each routine     |
| issue_id   | INTEGER | FOREIGN KEY REFERENCES issues(id) | Links to the associated issue          |
| routine    | TEXT    | NOT NULL                          | Suggested action or routine            |
| created_at | TEXT    |                                   | Timestamp when the routine was created |

### Folders Table

| Column | Type    | Constraints      | Description                         |
| ------ | ------- | ---------------- | ----------------------------------- |
| id     | INTEGER | PRIMARY KEY      | Unique identifier for each folder   |
| name   | TEXT    | NOT NULL, UNIQUE | Folder name for organizing projects |

### Item_Folders Table

| Column      | Type                 | Constraints                         | Description                                |
| ----------- | -------------------- | ----------------------------------- | ------------------------------------------ |
| item_id     | INTEGER              | FOREIGN KEY REFERENCES projects(id) | Links to a project                         |
| folder_id   | INTEGER              | FOREIGN KEY REFERENCES folders(id)  | Links to a folder                          |
| PRIMARY KEY | (item_id, folder_id) | COMPOSITE PRIMARY KEY               | Ensures unique project-folder combinations |

## Project Structure

```
terminal-task-manager/
├── main.py                 # Application entry point
├── controllers/            # Command handlers
│   ├── base_controller.py  # Base class for all controllers
│   ├── todos.py           # Todo management
│   ├── vsCodeProjectOpener.py # Project management
│   ├── mood_manager.py    # Mood and routine management
│   └── windows_settings.py # Windows utilities
├── database/              # Data persistence
│   ├── sql_data_store.py  # Database operations
│   └── migrations/        # Database schema
├── utils/                 # Utilities
│   ├── error_handler.py   # Error handling
│   └── helpers.py         # Common functions
├── enums/                 # Constants and enums
└── requirements.txt       # Dependencies
```

## Development

### Code Style

The project uses Black for code formatting with 100 character line length.

### Adding New Features

1. Create a new controller class inheriting from `BaseController`
2. Implement command methods and add to `command_dict`
3. Register the controller in `main.py`

### Database Migrations

Add new SQL files in `database/migrations/` following the naming pattern `V{version}__description.sql`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Commit with descriptive messages
5. Push to your fork
6. Create a pull request

## Troubleshooting

- **Database issues**: Delete `database/data_store.db` to reset
- **VSCode not opening**: Ensure VSCode is installed and in PATH
- **Permission errors**: Run as administrator for Windows settings features
- **Color issues**: Ensure your terminal supports ANSI colors

## Philosophy

This tool embodies a "mission framework" approach to problem-solving - creating systematic routines and solutions for recurring life challenges. It serves as both a productivity tool and a knowledge base for personal growth strategies.

---

**Note**: This is a personal productivity tool designed for Windows environments. Some features may not work on other operating systems.
