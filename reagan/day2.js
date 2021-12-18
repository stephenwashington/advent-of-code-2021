var fs = require("fs");
var text = fs.readFileSync("./input2.txt").toString("utf-8");
var textByLine = text.split("\n");

demo = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"];

// let horizontal = 0;
// let depth = 0;

// for (i = 0; i < textByLine.length; i++) {
//   let command = textByLine[i].split(" ");
//   switch(command[0]) {
//     case "forward":
//       horizontal+= parseInt(command[1]);
//       break;
//     case "down":
//       depth += parseInt(command[1]);
//       break;
//     case "up":
//       depth -= parseInt(command[1]);
//       break;
//   }
// }

// console.log('horizontal: ', horizontal);
// console.log('depth: ', depth);
// console.log(horizontal * depth);



let horizontal = 0;
let depth = 0;
let aim = 0;

for (i = 0; i < textByLine.length; i++) {
  let command = textByLine[i].split(" ");
  switch(command[0]) {
    case "forward":
      horizontal+= parseInt(command[1]);
      depth += aim * parseInt(command[1]);
      break;
    case "down":
      aim += parseInt(command[1]);
      break;
    case "up":
      aim -= parseInt(command[1]);
      break;
  }
}

console.log('horizontal: ', horizontal);
console.log('depth: ', depth);
console.log('aim: ', aim);
console.log(horizontal * depth);
