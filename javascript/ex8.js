const { log } = require('console');

function exercise8(fileName, lineLength){
    const fs = require('fs');
    const data = fs.readFileSync(fileName, "utf8").trim();
    const lines = data.replaceAll("\r", "").split("\n");

    let fullLine = "";
    for (let i = 0; i < lines.length; i++) {
        fullLine += lines[i] + " ";
    }

    let words = fullLine.split(" ");
    
    let justifiedLine = "";
    let justifiedText = [];

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


console.log(exercise8("../python/test_data/text1.txt", 50));