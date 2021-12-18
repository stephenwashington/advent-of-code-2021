var fs = require("fs");
var text = fs.readFileSync("./input3.txt").toString("utf-8");
var textByLine = text.split("\n");

demo = [
  '00100',
  '11110',
  '10110',
  '10111',
  '10101',
  '01111',
  '00111',
  '11100',
  '10000',
  '11001',
  '00010',
  '01010'
]

let mostOften = '';
let leastOften = '';

oxygen = [...textByLine];

for (i=0; i<textByLine[0].length; i++) {
  let count = 0;

  if (oxygen.length > 1 ){

    for (j=0; j < oxygen.length; j++) {
      count += (oxygen[j][i] > 0) ? 1 : -1;
    }

    // console.log('for col ', i, 'the count is: ', count);
    oxygen = oxygen.filter(input => input[i] == (count >= 0 ? 1 : 0)); 
    // scrubber = scrubber.filter(input => input[i] == (count >= 0 ? 0 : 1)); 

    console.log('oxygen: ', oxygen);
    // console.log('scrubber: ', scrubber);
  }
}

finalOxygen = parseInt(oxygen[0], 2);
console.log('finalOxygen: ', finalOxygen);


scrubber = [...textByLine];

for (i=0; i<textByLine[0].length; i++) {
  let count = 0;

  if (scrubber.length > 1) {
    for (j=0; j < scrubber.length; j++) {
      // console.log('textByLine[j][i]', scrubber[j][i]);
      count += (scrubber[j][i] > 0) ? 1 : -1;
    }

    // console.log('for col ', i, 'the count is: ', count);
    scrubber = scrubber.filter(input => input[i] == (count >= 0 ? 0 : 1)); 

    console.log('scrubber: ', scrubber);
  }
}

finalScrubber = parseInt(scrubber[0], 2);
console.log('finalScrubber: ', finalScrubber);

console.log('finalScrubber * finalOxygen: ', finalScrubber*finalOxygen);
