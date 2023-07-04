"use strict";
testFunction();
function testFunction() {
  x = 10; // causes an error because x is not declared
  console.log(x);
}