var x = myFunction(4, 3);
console.log(x);
function myFunction(a, b) {
  return a * b;
}

var v = 'Groove 1';
var stuff = "oustide stuff";

function  func(stuff) {
  console.log(v);
  stuff="reassigned a value to it";
  console.log(stuff);
}

func();
console.log(stuff);
