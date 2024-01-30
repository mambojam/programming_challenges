// # variable for punctuation (empty string) and variable for upper False
// # need to remove punctuation - if there is then save this in a variable and remove
// # check if first letter is upper case - if there is then save this in a boolean is letter A <= letter <= Z
// # need to lowercase .lower() -
// # capitalize IF there is a capital first letter -- set upper case to True
// # if first letter is vowel - add way to end of word
// # find the first vowel; slice the prefix, add to the end of word; add 'ay'
// # if upcase = True, then capitalize
// # add punctuation to the end


function exercise4(word) {
  let punctuation = ""; // to store the punctuation we strip
  let punc_string = ".,!?"; // the types of punctuation we're looking for
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

console.log(exercise4("Cream."));
console.log(exercise4("Organs!"));
