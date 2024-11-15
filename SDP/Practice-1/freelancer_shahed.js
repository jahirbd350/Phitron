let incomes = [1000, 2000, 3000];
let living_cost = 3000;

let savings = (array, living_cost) => {
  if (array.constructor != Array) {
    return "Invalid input!";
  }
  if (typeof living_cost != "number") {
    return "Invalid input!";
  }
  let saves = 0;
  for (let i = 0; i < array.length; i++) {
    if (array[i] > 3000) {
      saves += array[i] - array[i] * 0.2;
    } else {
      saves += array[i];
    }
  }
  saves -= living_cost;
  if (saves < 0) {
    return "Earn More!!";
  } else {
    return saves;
  }
};

let total_save = savings(incomes, living_cost);
console.log(total_save);
