import * as readlineSync from 'readline-sync';

interface ITodo {
  todos: Todo_T[];
  addTodo: (text: string) => void;
  removeTodo: (id: number) => void;
  toggleTodo: (id: number) => void;
  run: () => void;
}

export class Todo implements ITodo {
  todos: Todo_T[];
  constructor() {
    this.todos = [];
  }

  addTodo = (text: string) => {
    const todo = {
      id: this.todos.length + 1,
      text,
      done: false,
      createdAt: Date.now(),
    };
    this.todos = [...this.todos, todo];
  };

  removeTodo = (id: number) => {
    this.todos = this.todos.filter(todo => todo.id !== id);
  };

  toggleTodo = (id: number) => {
    this.todos = this.todos.map(todo => (todo.id === id ? { ...todo, done: !todo.done } : todo));
  };

  run = () => {
    let command = readlineSync.question('todo> ');

    while (command !== 'exit') {
      switch (command) {
        case 'add':
          let text = readlineSync.question('>>> ');
          while (text !== 'exit') {
            this.addTodo(text);
            text = readlineSync.question('>>> ');
          }
          this.printTodos();
          break;
        case 'toggle':
          let id = readlineSync.question('Enter the id of the todo to toggle: ');
          this.toggleTodo(Number(id));
          break;
        default:
          console.log('Unknown command. Please enter "add", "toggle", or "exit".');
      }
      command = readlineSync.question('todo> ');
    }

    console.log('Get out of Todo mode.');
  };

  private printTodos = () => {
    this.todos.forEach(todo => {
      console.log(`${todo.id}. ${todo.text} - ${todo.done ? 'done' : 'not done'}`);
    });
  };
}
