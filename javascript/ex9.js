// using a dictionary to map the alphabetised columns to numbers
let columns = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8};

// using a array of arrsys to represent the 8 possible moves a Knight can make
// e.g. first tuple = along one column, up two rows
let posMoves = [[1, 2], [1, -2], [2, 1], [2, -1], [-1, 2], [-1, -2], [-2, 1], [-2, -1]];

function ex9(start, end, moves){
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
    
console.log(ex9("a1", "f5", 2));
console.log(ex9("a1", "f5", 3));
console.log(ex9("b2", "c3", 1));
console.log(ex9("a1", "c3", 5));
// console.log(ex9("a1", "f5", 2));
// console.log(ex9("a1", "f5", 2));