// var person = { 
//     firstName: "Dhanashree", 
//     lastName: "Khandetod", 
//     age: 25, 
//     getFullName: function () { 
//         return this.firstName + ' ' + this.lastName 
//         } 
// };

// document.getElementById("p1").innerHTML = person.firstName; 
// document.getElementById("p2").innerHTML = person.lastName; 

// document.getElementById("p3").innerHTML = person["firstName"];
// document.getElementById("p4").innerHTML = person["lastName"];

// document.getElementById("p5").innerHTML = person.getFullName();
// console.log(person.firstName)


// Create an object using object literal:
const myObj = {
    name: 'Anthony Edward Stark',
    alias: 'Iron Man',
    gender: 'male',
    education: 'MIT',
    affiliation: {
      current: 'Avengers'
    },
    creators: ['Stan Lee', 'Larry Lieber', 'Don Heck', 'Jack Kirby'],
    status: {
      alignment: 'good'
    }
  }
  
  
  // Accessing object properties with dot notation:
  // First: name of the object.
  // Second: name of the property to access.
  // Third: dot character between the object and property.
  console.log(myObj.name)
    
  console.log(myObj.alias)
 
  
  
  // Accessing deeper object properties:
  // Access the "current" property that exists
  // in nested object assigned to "affiliation" property
  console.log(myObj.affiliation.current)
  
  
  // Accessing array items in objects:
  // Access the first item inside the array
  // assigned to "creators" property.
  console.log(myObj.creators[0])
  
  