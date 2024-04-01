"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.Todo = void 0;
const readlineSync = __importStar(require("readline-sync"));
class Todo {
    todos;
    constructor() {
        this.todos = [];
    }
    addTodo = (text) => {
        const todo = {
            id: this.todos.length + 1,
            text,
            done: false,
            createdAt: Date.now(),
        };
        this.todos = [...this.todos, todo];
    };
    removeTodo = (id) => {
        this.todos = this.todos.filter(todo => todo.id !== id);
    };
    toggleTodo = (id) => {
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
    printTodos = () => {
        this.todos.forEach(todo => {
            console.log(`${todo.id}. ${todo.text} - ${todo.done ? 'done' : 'not done'}`);
        });
    };
}
exports.Todo = Todo;
