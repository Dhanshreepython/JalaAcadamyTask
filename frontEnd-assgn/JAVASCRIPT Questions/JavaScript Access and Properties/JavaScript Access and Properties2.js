const person = {
    fullName: function() {
      return this.firstName + " " + this.lastName;
    }
  }
  const person1 = {
    firstName:"John",
    lastName: "Doe"
  }
  const person2 = {
    firstName:"Mary",
    lastName: "Doe"
  }
  document.getElementById("demo").innerHTML = person.fullName.call(person1);



  const fruit = {
    fullName: function() {
      return this.firstName + " " + this.lastName;
    }
  }
  
  const fruit1 = {
    firstName:"Custard",
    lastName: "apple"
  }
  
  document.getElementById("demo2").innerHTML = person.fullName.apply(fruit1);