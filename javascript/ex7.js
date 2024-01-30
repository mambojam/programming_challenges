const { log } = require('console');

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


console.log(exercise7("functions.txt"));

//     no_comment_funcs = []
//     with open(file, 'r') as file:
//         text = file.read()
//         file_lines = text.splitlines()

//     for i in range(len(file_lines)):
//         if file_lines[i].startswith("def "):
//             if not file_lines[i-1].startswith("#"):
//                 func_name = file_lines[i][4:]
//                 func_name_no_par = ""
//                 for char in func_name:
//                     if char == "(":
//                         break
//                     else:
//                         func_name_no_par += char
//                 func_name = func_name_no_par
//                 no_comment_funcs.append(func_name)

//     return no_comment_funcs