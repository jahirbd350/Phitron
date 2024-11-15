let numbers = [1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10];

const useSet = (numbers) => {
  return [...new Set(numbers)];
};

let result = useSet(numbers);
console.log(result);
