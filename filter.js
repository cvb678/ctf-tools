"use strict";
//filter unwanted characters from text

let txt = "SO213._ME@!\n\n #TEXT";

let lowerBound = "A".charCodeAt(0);
let upperBound = "Z".charCodeAt(0);

let checkBoundaries = function(uBound, lBound, char) {
  let code = char.charCodeAt(0);

  if((code > uBound || code < lBound) && char !== " ") {
    return -1;
  }

  return 1;
}

txt = txt.split("")
        .filter(item => checkBoundaries(upperBound, lowerBound, item) === 1)
        .join("");

console.log(txt);

//node substitution.js > txt
