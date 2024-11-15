let numbers = [1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10];

const biggestNumber = (array) => {
  let bigNo = array[0];
  for (let i = 0; i < array.length; i++) {
    if (array[i] > bigNo) {
      bigNo = array[i];
    }
  }
  return bigNo;
};

let result = biggestNumber(numbers);
console.log(result);
