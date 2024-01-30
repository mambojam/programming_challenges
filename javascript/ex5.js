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
      morseMessage += morseCodeObj[upperCase[i]] + " "; // concatenate string to build message
    }
  }
  morseMessage = morseMessage.slice(0, -1); // strip the last letter which will be a space

  return morseMessage;
}

console.log(exercise5("Hello!"));
console.log(exercise5("Dan"));
