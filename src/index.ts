// import { Todo } from './controllers/Todo';
import * as readlineSync from 'readline-sync';

// const todo = new Todo();

// const cmd = readlineSync.question('bardala> ');

// if (cmd === 'todo') {
//   todo.run();
// } else if (cmd === 'exit') {
//   console.log('Bye!');
// } else {
//   console.log('Unknown command. Please enter "todo" or "exit".');
// }

// test readline-sync
const name = readlineSync.question('What is your name? ');
console.log(`Hi, ${name}!`);
