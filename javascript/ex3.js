let myList = [1, 2, 3, 4, 5];

function exercise3(list){
  let newList = [[]];
  for (let i = 0; i < list.length; i++) {
    for (let j = i + 1; j < list.length + 1; j++) {
      newList.push(list.slice(i, j));
    }
  }
  return newList;
}

console.log(exercise3(myList));
