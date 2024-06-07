const prompt = require("prompt-sync")({sigint:true});

function sumOf(a, b) {
    let x = a+b;
    console.log(`The sum of ${a} and ${b} is ${x}`);
}
function productOf(a, b) {
    let x = a*b;
    console.log(`The product of ${a} and ${b} is ${x}`);
}
function diffOf(a, b) {
    let x = a-b;
    console.log(`The difference of ${a} and ${b} is ${x}`);
}


function main() {
    let a = Number(prompt("Enter value 1: "));
    let b = Number(prompt("Enter value 2: "));
    sumOf(a, b);
    productOf(a, b);
    diffOf(a, b);
}

main()