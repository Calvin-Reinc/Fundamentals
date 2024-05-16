// Task 3: Implement a program that takes a numeric input from the user and 
// prints all numbers from 1 to that number. However, for multiples of three, 
// print "Fizz" instead of the number, and for the multiples of five, print "Buzz". 
// For numbers which are multiples of both three and five, print "FizzBuzz".

function FizzBuzz(number) {

    for (let i = 1; i < number+1; i++) {
        if (i%3==0 && i%5==0) {
            console.log("FizzBuzz");
        }
        else { 
            if (i%3==0) {
                console.log("Fizz");
            } else {
                if (i%5==0) {
                    console.log("Buzz");
                } else {
                console.log(i);
                }
            }
            
        }
    }
}

const prompt = require("prompt-sync")({sigint:true});
var number = prompt("Enter a number: ");
number = Number(number);
FizzBuzz(number);
