const prompt = require("prompt-sync")({sigint:true});


class Rectangle {
    constructor(width, height) {
        this.width = width;
        this.height = height;
    }
    area() {
        let area = Number(this.height * (this.width));
        console.log(`The area of the rectangle is ${area}`);
    }
    rectangle() {
        for (let i = 0; i < this.height; i++) {
            console.log("*".repeat(this.width));
        }
    }
}

function main() {
    let a = prompt("enter width: ");
    let b = prompt("enter height: ");
    let myTest = new Rectangle(a, b);
    myTest.rectangle();
    myTest.area()
}

main()