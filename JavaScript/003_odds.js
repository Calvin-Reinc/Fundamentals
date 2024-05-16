// # Task 2: Write a program that asks the user to enter a number. 
// # Check if the number is even or odd. Then, print an appropriate message to the user.

function odds(number) {
    if (number % 2 == 0) {
        console.log("That's an even number.");
    } else {
        console.log("That's an odd number.");
    }
}

const prompt = require("prompt-sync")({sigint:true});
var number = prompt("Enter a number: ");
number = Number(number);
odds(number);
