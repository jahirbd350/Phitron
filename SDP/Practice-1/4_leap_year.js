const r1 = require("readline-sync");
const yr = r1.question("Enter the year: ");

function leapYear(year) {
  return (year % 4 == 0 && year % 100 != 0) || year % 400 == 0;
}

let lpyr = leapYear(yr);
// console.log(lpyr);
if (lpyr) {
  console.log("This is leap year!!");
} else {
  console.log("This is not leap year!!");
}
