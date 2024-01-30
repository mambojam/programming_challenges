// # Exercise 1 - Smallest Fraction Terms

function exercise1(num, den) {
  // find whether num or den is lower than the other and store in
  // a variable called lower
  let lower;
  if (num < den) {
    lower = num;
  }
  else if (den < num) {
    lower = den;
  }
  else {
    return "That's a whole number";
  }


  let gCD; // create an empty variable where we'l store the greatest common divisor
  // starting from lower and working backwards, modulo num and den by n
  // if both num and den % n == 0 (they are divisible by n), we have found the
  // greatest common divisor
  for (let n = lower; n >= 0; n--) {
    if (num % n == 0 && den % n == 0) {
      gCD = n;
      break;
    }
  }
  // divide num and den by gCD to find the lowest common denominator
  num = num/gCD
  den = den/gCD
  lCD = [num, den]
  return lCD
}

console.log(exercise1(122, 120));
console.log(exercise1(7, 12));
console.log(exercise1(15, 3));
console.log(exercise1(21, 28));
