function order() {
    const prompt = require("prompt-sync")({sigint:true});

    let userFood = prompt("What is your favourite food: ");
    let foodList = [];
    foodList.push(userFood)
    let myBool = true;

    for (let i=0; i<foodList.length; i++) {
        console.log(String(foodList));
    }
}


order()