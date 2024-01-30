const fs = require('fs');


// exercise 1
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
  let gCD; // create an empty variable where we'll store the greatest common divisor
  // starting from lower and working backwards, modulo num and den by n
  // if both num and den % n == 0 (they are divisible by n),
  // then we have found the greatest common divisor
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


function exercise2(day, month, year) {
  // % 100 finds the last two digits, the decade year
  let decade = year % 100;
  // multiply day and month and test if it is equal to the last two digits
  if (day * month == decade) {
    return true;
  }
  else {
    return false;
  }
}


function exercise3(list){
  // create a list containing one list, an empty list
  let newList = [[]];
  // iterate through the list starting with point i at index 0
  for (let i = 0; i < list.length; i++) {
    // set point j to start one index ahead of i and iterate to the end of the list
    for (let j = i + 1; j < list.length + 1; j++) {
      // for each iteration, append the slice of our list from point i to j to the list
      newList.push(list.slice(i, j));
    }
  }
  return newList; // return the list containing all sublists
}

function exercise4(word) {
  let punctuation = ""; // to store the punctuation we strip
  let punc_string = "!?.(),;:'\"-_&<>#~[]*^%$£"; // the types of punctuation we're looking for
  let vowels = ["a", "e", "i", "o", "u"]; // the vowels
  let upper = false; // a switch to tell us if word starts with upperCase
  let translation = ""; // our string to store translation

// if first letter is uppercase, switch upper to true and transform word to lowercase
  if (word[0] == word[0].toUpperCase()) {
    upper = true
    word = word.toLowerCase();
  }
// test whether the last letter is a punctuation mark if it is store it
  for (let i = 0; i < punc_string.length; i++) {
    if (punc_string[i] == word[word.length-1]) {
      punctuation += punc_string[i];
    }
  }
// cut the length (either 0 or 1) off the end of the word to remove punctuation
  word = word.slice(0, word.length-punctuation.length)

// check whether word starts with a consonants (letter is NOT in vowels)
  if (!vowels.includes(word[0])){
    let consonants = ""; // create a variable for our consonants
    for (let i = 0; i < word.length; i++){ // check through all the letters
      if (!vowels.includes(word[i])){ // if letter is a consonant
        consonants += word[i]; // add it to the consonants string
      }
      else { break; } // once we hit a vowel, stop
    }
    // chop the consonants off the start, add them on the end, add "ay" and the punctuation back on
    translation = word.slice(consonants.length) + consonants + "ay" + punctuation;
  }
  // if it starts with a vowel, add "way" and punctuation
  else {
    translation = word + "way" + punctuation;
  }
// if it started with a caps, change the first letter back to caps, chop off the
// lower and stick the caps back on
  if (upper == true) {
    let capitalize = translation[0].toUpperCase();
    translation = translation.slice(1);
    translation = capitalize + translation;
  }

  return translation;
}

// exercise 5
// create an object to store all the morse_code values according to their number or letter
let morseCodeObj = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..",
    "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": ".._", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..",
    "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..",
    "9": "----.", "0": "-----"};


function exercise5(userInput){
  // create an empty string which we will concatenate our message into
  let morseMessage = "";
  // convert user_input to upper_case
  let upperCase = userInput.toUpperCase();
  // loop through letters in the uppercase string
  for (let i = 0; i < upperCase.length; i++) {
    if (morseCodeObj.hasOwnProperty(upperCase[i])) { // if the letter corresponds to a key in the obj
      morseMessage += morseCodeObj[upperCase[i]] + " "; // concatenate string to build message, separate letters by spaces
    }
  }
  morseMessage = morseMessage.slice(0, -1); // strip the last letter which will be a space

  return morseMessage;
}
// create dictionaries for the single digits, teens, tens and hundreds
let digits = {"1": "one", "2": "two", "3": "three", "4": "four", "5": "five",
          "6": "six", "7": "seven", "8": "eight", "9": "nine", "0": ""}

let teens = {"11": "eleven", "12": "twelve", "13": "thirteen", "14": "fourteen", "15": "fifteen",
         "16": "sixteen", "17": "seventeen", "18": "eighteen", "19": "nineteen", "0": ""}

let tens = {"1": "ten", "2": "twenty", "3": "thirty", "4": "forty", "5": "fifty",
        "6": "sixty", "7": "seventy", "8": "eighty", "9": "ninety", "0": ""}

let hundreds = {"1": "a hundred", "2": "two hundred", "3": "three hundred", "4": "four hundred", "5": "five hundred",
            "6": "six hundred", "7": "seven hundred", "8": "eight hundred", "9": "nine hundred", "0": ""}

function exercise6(num){
    let strNum = num.toString(); // transform the input num to string
    let spelling_out = ""; // create an empty string to write the spelling out into

    if (num == 0){
        return "zero"
    }
    // check length and draw corresponding values from the dictionary keys
    let length = strNum.length;
    if (length == 3){ 
      spelling_out += hundreds[strNum[length-3]] + " and ";
    }
    if (length >= 2) {
      if (10 < num % 100 && num % 100 < 20) {
        spelling_out += teens[strNum[length-2] + strNum[length-1]];
        return spelling_out;
      }
      else if (num % 100 == 10) {
        spelling_out += tens[1];
        return spelling_out;
      }
      else {
          spelling_out += tens[strNum[length-2]] + "-";
      }
    }
    if (length >= 1) {
      spelling_out += digits[strNum[length-1]]
    }
    if (length > 3 || num < 0) {
      return "please enter a number between 0 and 999";
    }
    return spelling_out;
}

function exercise7(file){
  let noCommentFunctions = [];
  
  const fs = require('fs');
  const data = fs.readFileSync(file, "utf8");
  const lines = data.replaceAll("\r", "").split("\n");

  for ( let i = 0; i < lines.length; i++ ) {
      if (lines[i].startsWith("function ")) {
          if (lines[i-1] == undefined || !(lines[i-1].startsWith("//"))){
              funcName = lines[i].slice(9, lines[i].length);
              let noParName = ""
              for (let i = 0; i < funcName.length; i++) {
                  if ( funcName[i] == "(" ){
                      break;
                  }
                  else {
                      noParName += funcName[i];
                  }
              }
              noCommentFunctions.push(noParName);
          }
      }

  }
  return noCommentFunctions;
}


function exercise8(fileName, lineLength){
  const fs = require('fs'); 
  const data = fs.readFileSync(fileName, "utf8").trim(); // read file and trip whitespace
  const lines = data.replaceAll("\r", "").split("\n"); // get the lines in a list

  // create an empty string, loop through the list of lines to concatenate a single line string
  let fullLine = "";
  for (let i = 0; i < lines.length; i++) {
      fullLine += lines[i] + " ";
  }
  // list of all the words
  let words = fullLine.split(" ");
  
  let justifiedLine = ""; // empty string to build the lines up to max length 
  let justifiedText = []; // empty list to store lines once we reach max

  for (let i = 0; i < words.length; i++) {
      if ((justifiedLine + words[i]).length <= lineLength) {
          justifiedLine = justifiedLine + words[i] + " ";
          if (words[i] == words[words.length-1]){
              justifiedText.push(justifiedLine.trim());
          }
      }
      else {
          justifiedText.push(justifiedLine.trim());
          justifiedLine = words[i] + " ";
          if (words[i] == words[words.length-1]) {
              justifiedText.push(justifiedLine);
          }
      }
  }
  return justifiedText;
}


// ex9 
// using a dictionary to map the alphabetised columns to numbers
let columns = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8};

// using a array of arrsys to represent the 8 possible moves a Knight can make
// e.g. first tuple = along one column, up two rows
let posMoves = [[1, 2], [1, -2], [2, 1], [2, -1], [-1, 2], [-1, -2], [-2, 1], [-2, -1]];

function exercise9(start, end, moves){
    // transform the input to [column, row] format as nums in list
    let position = [columns[start[0]], parseInt(start[1])];
    let endPosition = [columns[end[0]], parseInt(end[1])];

    console.log(position);
    console.log(endPosition);

    // create a dictionary where key = move_num and value = list of pos_positions starting move 0 = position
    let posPositions = {0: [position]}

    // limit the number of moves
    for (let num = 0; num < moves; num++){
        let moveNum = num + 1;  // start from 1 (not 0)
        posPositions[moveNum] = [];  // create a new key in the dictionary for this move

        // iterate through the positions after each move
        for (let pos = 0; pos < posPositions[num].length; pos++) {

            // adding the possible moves to the current position
            for (let move = 0; move < posMoves.length; move++) {
                let newPosition = [posPositions[num][pos][0] + posMoves[move][0], posPositions[num][pos][1] + posMoves[move][1]];
                // is it a match for the end point?   
                if (newPosition[0] == endPosition[0] && newPosition[1] == endPosition[1]) {
                    console.log("new position" + newPosition);
                    console.log(posPositions);
                    return true;
                }
                // add new position to the dictionary if it is not out of bounds
                else if (0 < newPosition[0] && newPosition[0] <= 8 
                    && 0 < newPosition[1] && newPosition[1] <= 8)
                       {
                        posPositions[moveNum].push(newPosition);
                      }
                }        
        }
    }
    
    return false;
}



function twoDArray(listOfStrings) {
    let newEnv = [];
    for (let i = 0; i < listOfStrings.length; i++) {
        let stringList = [];
        for (let j = 0; j < listOfStrings[i].length; j++) {
            stringList.push(listOfStrings[i][j]);
        }
        newEnv.push(stringList);
    }
    return newEnv;
}

let neighbourPos = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]];

function findNeighbours(cell, environment) {
    let neighbours = [];

    for (let i = 0; i < neighbourPos.length; i++) {
        let neighbour = [cell[0] + neighbourPos[i][0], cell[1] + neighbourPos[i][1]];
        
        if (0 <= neighbour[0] && neighbour[0] < environment.length 
            && 0 <= neighbour[1] && neighbour[1] < environment[0].length) {
                neighbours.push(neighbour);
            }
    }
    return neighbours;
}

function exercise10(listOfStrings) {
    // turn the list of strings into a 2d array
    let newEnv = twoDArray(listOfStrings);
    
    // create a copy of the environment 
    let copiedEnv = newEnv.map(innerArray => innerArray.slice());

    // working through each element by row and column
    for (let i = 0; i < newEnv.length; i++ ) {
        for (let j = 0; j < newEnv[i].length; j++ ) {
            // keep count of species
            let speciesXCount = 0;
            let speciesOCount = 0;
            // give the current thing y and x co-ordinates
            let cell = [i, j];
            // find neighbours
            let neighbours = findNeighbours(cell, newEnv);
            // count the number of different neighbouring species
            neighbours.forEach((neighbour) => {
                let y = neighbour[0];
                let x = neighbour[1];
                if (newEnv[y][x] === "X") {
                    speciesXCount += 1;
                }
                else if (newEnv[y][x] === "O") {
                    speciesOCount += 1;
                }                  
            });

            let living = speciesOCount + speciesXCount;
            // check the conditions and change the cells in the copy
            if (newEnv[i][j] === "." && living >= 2 && living < 6) {
                if (speciesXCount < speciesOCount) {
                    copiedEnv[i][j] = "O";
                } else if (speciesOCount < speciesXCount) {
                    copiedEnv[i][j] = "X";
                }
            } else if (living > 6) {
                copiedEnv[i][j] = ".";
            } else if (newEnv[i][j] === "X" && (speciesXCount < 3 || speciesXCount < speciesOCount)) {
                copiedEnv[i][j] = ".";
            } else if (newEnv[i][j] === "O" && (speciesOCount < 3 || speciesOCount < speciesXCount)) {
                copiedEnv[i][j] = ".";
            }
        }
    }
    // copy back into an array of strings
    let changedEnv = copiedEnv.map(row => row.join(''));
    return changedEnv;
}


module.exports = {
    // Exercise 1
    exercise1: exercise1,

    // Exercise 2
    exercise2: exercise2,

    // Exercise 3
    exercise3: exercise3,

    // Exercise 4
    exercise4: exercise4,

    // Exercise 5
    exercise5: exercise5,

    // Exercise 6
    exercise6: exercise6,

    // Exercise 7
    exercise7: exercise7,

    // Exercise 8
    exercise8: exercise8,

    // Exercise 9
    exercise9: exercise9,

    // Exercise 10
    exercise10: exercise10,
}
