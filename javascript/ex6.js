let digits = {"1": "one", "2": "two", "3": "three", "4": "four", "5": "five",
          "6": "six", "7": "seven", "8": "eight", "9": "nine", "0": ""}

let teens = {"11": "eleven", "12": "twelve", "13": "thirteen", "14": "fourteen", "15": "fifteen",
         "16": "sixteen", "17": "seventeen", "18": "eighteen", "19": "nineteen", "0": ""}

let tens = {"1": "ten", "2": "twenty", "3": "thirty", "4": "forty", "5": "fifty",
        "6": "sixty", "7": "seventy", "8": "eighty", "9": "ninety", "0": ""}

let hundreds = {"1": "a hundred", "2": "two hundred", "3": "three hundred", "4": "four hundred", "5": "five hundred",
            "6": "six hundred", "7": "seven hundred", "8": "eight hundred", "9": "nine hundred", "0": ""}

function exercise6(num){
    let strNum = num.toString();
    let spelling_out = "";

    if (num == 0){
        return "zero"
    }

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

console.log(exercise6(616));
console.log(exercise6(15));
console.log(exercise6(119));
console.log(exercise6(510));
console.log(exercise6(0));
console.log(exercise6(625));
console.log(exercise6(999));
console.log(exercise6(1000));
console.log(exercise6(1));
console.log(exercise6(19));
console.log(exercise6(213));
console.log(exercise6(514));
console.log(exercise6(615));
console.log(exercise6(317));
console.log(exercise6(819));
