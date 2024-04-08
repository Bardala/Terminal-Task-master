I want to create a project which run in command line and it will be a about my life styles, todos, my daily routines, my goals, my dreams, my plans, my ideas, my thoughts, my notes, my projects, my works, my hobbies, my interests, my skills, my experiences, my knowledge, my education, my career, my achievements, my failures, my problems, my solutions, my decisions, my mistakes, my lessons, my improvements, my changes, my challenges, my progress, my success, my happiness, my sadness, my emotions, my feelings, my relationships, my friends, my family, my relatives, my colleagues, my mentors, and I will use python.

The project will run in cmd by typing `py filename.py`.
Once I run the project, I can type any command which I have made to do something, ex:

- when I type `todo`, it will show me my todos.
- when I type `add_todo`, it will add a todo.

The program will have the ability to:

- notify me.
- open other programs.
- set alarms.
- open projects in vscode.
- open websites.
  It will have a lot of permissions to do things in my computer.

# User Stories:

- As a user, I want to add a todo.
- As a user, I want to see my todos.
- As a user, I want to delete a todo.
- As a user, I want to update a todo.
- As a user, I want to make a todo as done.
- As a user, I can write a routine to do when feeling boring, bad, not self-controlled...
- As a user, I can write a routine to do when I face a problem in coding, in life, in work, in study...
- As a user, I can write a routine to do when I face a problem in relationship, in family, in friends, in colleagues...
- As a user, I can write a routine to do when I face a problem in health, in mental, in physical, in emotional...
- As a user, I can set algorithms about how to manage my time.
- As a user, I can set algorithms about how to manage something I don't love to do.
- As a user, I can write my thoughts to benefit myself in the future.
- As a user, I can write ways which I use to solve a specific problem.
- As a user, I can write my plans to do in the future.
- As a user, I can search about algorithms to solve a specific current problem.
- As a user, I can write command to show me the instructions of the program.

# Features:

- Add a todo.
- Write a routine.
- Set algorithms.
- Write thoughts.
- Write ways to solve a problem.
- Write plans.
- Search algorithms.
- Show instructions.

# Technologies:

- Python
- cmd
- vscode
- git
- github

# Plan:

- Day 1: Create a project structure.
  - Create a main file.
  - Create a todo file.
  - Create a routine file.
  - Create an algorithm file.
  - Create a thought file.
  - Create a way to solve a problem file.
  - Create a plan file.
  - Create a search algorithm file.
- Day 2: Create a todo feature.
- Day 3: Create a routine feature.
- Day 4: Create an algorithm feature.
- Day 5: Create a thought feature.
- Day 6: Create a way to solve a problem feature.
- Day 7: Create a plan feature.
- Day 8: Create a search algorithm feature.
- Day 9: Create a notification feature.
- Day 10: Create an open program feature.
- Day 11: Create an alarm feature.
- Day 12: Create an open vscode project feature.
- Day 13: Create an open website feature.
- Day 14: Create a permission feature.
- Day 15: Create a user interface feature.

I will use OOP to create this project.

# demo:

## The program will start like this:

```sh
> bardala
```

## To Enter to do mode, you should write `> todo`:

```sh
bardala> todo
```

## then the program will show you the todos in a table if exist, and will start the todo mode:

```sh
todo>
```

## To add a todo, you should write `todo> add`, then the program will start a new line to write the todo:

```sh
todo> add
add new todo
>>> todo1
>>> todo2
>>> todo3
>>> done
```

## When I finish writing the todos, the program will show me the todos in a table:

| id  | todo  | status | created                  |
| --- | ----- | ------ | ------------------------ |
| 1   | todo1 | done   | 2021-09-01 > 09:00:00 PM |
| 2   | todo2 | todo   | 2021-09-01 > 09:01:05 PM |
| 3   | todo3 | done   | 2021-09-01 > 09:02:10 PM |

```sh
todo>
```

## When I write `>show` the program will show me the todos in a table:

```sh
todo> show
```

| id  | todo  | status | created                  |
| --- | ----- | ------ | ------------------------ |
| 1   | todo1 | done   | 2021-09-01 > 09:00:00 PM |
| 2   | todo2 | todo   | 2021-09-01 > 09:01:05 PM |
| 3   | todo3 | done   | 2021-09-01 > 09:02:10 PM |

---

## To delete todo you should write `> delete id`:

```sh
todo> deleteTodo 1
```

## To update todo you should write `> update id`, then the program will start a new line to write the new todo:

```sh
todo> update 2
```

## To make a todo as done you should write `> done id`:

```sh
todo> done 2
```
