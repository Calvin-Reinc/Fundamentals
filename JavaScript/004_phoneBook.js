const prompt = require("prompt-sync")({sigint:true});
let phoneList = {}

function add_phonebook() {
    let myBool = true;
    let userName = "";
    let userNumber = "";
    while (myBool) {
        userName = prompt("Enter your name: ");
        userNumber = prompt("Enter your phone number:");
        phoneList[userName] = userNumber
        myBool = false
    }
    return userName;
}

function delete_phone(userName) {
    delete phoneList[userName];
    return phoneList;
}

function search_phone() {
    let lookFor = prompt("Search by name: ");
    console.log("searching...");
    if (phoneList[lookFor]) {
        let result = phoneList.include(lookFor);
    }
    else { 
        result = false;
    }

    if (result) {
        console.log(`${lookFor} - ${phoneList[lookFor]}`);
    } else {
        console.log("Contact not found.");
    }
}

function view_phone() {
    for (let key in phoneList) {
        console.log(`${key} - ${phoneList[key]}`);
    }
}

function main() {
    let myBool = true;
    let userName, userNumber
    console.log("---- PhoneBook ----")
    while (myBool) {
        console.log("1. Add new contact"+"\n"+"2. Delete contact"+"\n"+"3. Search"+"\n"+"4. Display contacts"+"\n"+"Q to quit");
        let work = (prompt("select option(Use numbers): "));
        if (work.charAt(0) == "1") {
            userName = add_phonebook();
            console.log(`${userName}:  ${phoneList[userName]}\n Contact saved.`);
        } else {
            if (work.charAt(0) == "2") {
                userName = prompt("Search by name: ");
                delete_phone(userName);
                console.log("Deleted!")
            } else {
                if (work.charAt(0) == "3") {
                    search_phone();
                } else {
                    if (work.charAt(0).toUpperCase() == "Q") {
                        myBool = false;
                    } else {
                        if (work.charAt(0) == "4") {
                            view_phone()
                        } else {
                            console.log("Select a valid option.(Use number to identify)");
                        }
                    }
                }
            }
        }
    }
}

main()