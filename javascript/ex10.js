let input = ['XX......',
             'XX....O.',
             '.....OOO'];


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
            // look at the current cell again
            // copiedEnv[i][j] = newEnv[i][j];
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

console.log(exercise10(input));