// var myname = "Md Jahirul Islam";

// console.log(myname);

const numbers = [
  1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
];

const oddEven = (array) => {
  let evenNums = [];
  let oddNums = [];

  for (let i = 0; i < array.length; i++) {
    const element = array[i];
    if (element % 2) {
      oddNums.push(element);
    } else {
      evenNums.push(element);
    }
  }
  return oddNums;
};

const result = oddEven(numbers);

console.log(result);
