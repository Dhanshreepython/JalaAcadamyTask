// 4. Create a Counter with the help of getter and setter accessors
 // Create an object:
 const person = {
    firstName: "John",
    lastName: "Doe",
    language: "en",
    get lang() {
        return this.language;
    }
    };

    // Display data from the object using a getter:
    document.getElementById("demo").innerHTML = person.lang;


    // Create an object:
    const person1 = {
        firstName: "John",
        lastName: "Doe",
        language: "NO",
        /**
         * @param {string} value
         */
        set lang(value) {
            this.language = value;
        }
        };
    
        // Set a property using set:
        person1.lang = "en";
    
        // Display data from the object:
        document.getElementById("demo1").innerHTML = person1.language;