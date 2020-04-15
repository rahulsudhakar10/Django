var oneChar = document.querySelector("#one");
var twoChar = document.querySelector("#two");
var threeChar = document.querySelector("#three");

oneChar.addEventListener("mouseover", function(){
  oneChar.textContent= "Hello World";
  oneChar.style.color ="red";
});

oneChar.addEventListener("mouseout", function(){
  oneChar.textContent= "Houer me";
  oneChar.style.color ="black";
});

twoChar.addEventListener("click", function(){
  twoChar.textContent= "clicked me";
});


threeChar.addEventListener("dblclick", function(){
  threeChar.textContent= "double clicked me";
});
