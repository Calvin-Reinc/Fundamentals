const prompt = require("prompt-sync")({sigint:true});

class BankAccount {
    constructor(balance) {
        this._balance = balance;
    }

    balance() {
        let formattedBalance = this._balance.toFixed(2);
        console.log(`Your current balance is R${formattedBalance}`);
    }

    isDigit(amount) {
        return /^\d+$/.test(amount);
    }

    deposit() {
        let deposit = Number(prompt("How much do you want to deposit: "));
        if (this.isDigit(deposit)) {
            this._balance = this._balance + deposit;
        } else {
            console.log("An exception occurred. Please try again.");
        }
    }

    withdraw() {
        let withdrawal = Number(prompt("How much do you want to deposit: "));
        if (this.isDigit(withdrawal)) {
            if (withdrawal < this._balance) {
            this._balance = this._balance - withdrawal;
            } else {console.log("You have insufficient balance.")}
        } else {
            console.log("An exception occurred. Please try again.");
        }
    }
}

function main() {
    let balanceAmount = 0.00;
    let bank = new BankAccount(balanceAmount);
    let bankOn = true;

    while (bankOn) {
        bank.balance();
        console.log("1. Deposit"+"\n"+
                    "2. Withdraw"+"\n"+
                    "3. Quit");
        let status = Number(prompt("what do you want to do.(Select a number): "));
        if (bank.isDigit(status)) {
            if (status == 1) {
                bank.deposit();
            }
            if (status == 2) {
                bank.withdraw();
            }
            if (status == 3) {
                bank.balance();
                console.log("GoodBye. See you soon.");
                bankOn = false;
            }
        } else {
            console.log("Select a valid choice.");
        }
    }
}

main()