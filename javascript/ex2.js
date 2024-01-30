function exercise2(day, month, year) {
  let decade = year % 100;
  if (day * month == decade) {
    return true;
  }
  else {
    return false;
  }
}

console.log(exercise2(5, 6, 1940));
