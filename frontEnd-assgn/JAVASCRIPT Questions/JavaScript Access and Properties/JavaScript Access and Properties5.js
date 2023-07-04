
function Person(first, last, age, eye) {
  this.firstName = first;
  this.lastName = last;
  this.age = age;
  this.eyeColor = eye;
}

Person.prototype.nationality = "Marathi";

const myFather = new Person("Manohar", "khandetod", 50, "blue");
document.getElementById("demo").innerHTML =
"The nationality of my father is " + myFather.nationality; 




// Using an object constructor
function Person(first, last, age, eye) {
    this.firstName = first;
    this.lastName = last;
    this.age = age;
    this.eyeColor = eye;
  }
  
  const mybrother = new Person("John", "Doe", 26, "blue");
  const myMother = new Person("Sally", "Rally", 48, "green");
  
  document.getElementById("demo1").innerHTML =
  "My Brother is " + mybrother.age + " And My mother is " + myMother.age; 