var person = {firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"};
console.log(person["firstName"])

var car  = {a:"rahul",b:[1,2,3],c:{inside:[1 ,5,6]}}
console.log(car["a"]);
console.log(car["b"][1]);
console.log(car["c"]["inside"][2]);

car["a"]= "bday";
console.dir(car);

for (key in car) {
  console.log(key);
}

var obj = {
  prop:"rahul bday",
  greet:function inside() {
    console.log("Tommorrow is "+this.prop);
  }

  }

  obj.greet();
    console.log(obj["prop"]);
