var fs = require("fs");
var text = fs.readFileSync("./input1.txt").toString('utf-8');
var textByLine = text.split("\n");
var inputArray = textByLine.map(x => parseInt(x));

var demo = [
199,
200,
208,
210,
200,
207,
240,
269,
260,
263
]


let windowIncreases = []; 

for (i = 0; i < inputArray.length - 2; i++) {
  var sum = inputArray[i] + inputArray[i + 1] + inputArray[i + 2];

  windowIncreases.push(sum)
}


let numIncreases = 0; 

for (i = 1; i < windowIncreases.length; i++) {
  if (windowIncreases[i] > windowIncreases[i - 1]) {
    numIncreases++;
  }
}

console.log(numIncreases)
