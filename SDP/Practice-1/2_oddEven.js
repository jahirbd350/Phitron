const r1 = require("readline-sync");
const number = r1.question("Enter The Number: ");

if (number % 2) {
  console.log("This is odd number!!!");
} else {
  console.log("This is even number!!!");
}
