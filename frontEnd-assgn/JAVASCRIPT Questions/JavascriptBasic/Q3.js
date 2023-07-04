let text = "";
for (let i = 0; i < 10; i++) {
  text += i + "<vr> | ";
}
document.getElementById("demo").innerHTML = text;


const person = {fname:"John", lname:"Doe", age:25}; 

let txt = "";
for (let x in person) {
  txt += person[x] + " ";
}

document.getElementById("demo1").innerHTML = txt;