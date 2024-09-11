const prompt = require("prompt-sync")({sigint:true});

function palindrome(word) {
    let count = 0;
    let p_word = "";
    for (let i = 0; i < word.length; i++) {
        console.log(word[i], word[word.length-1-i]);
        if (word[i] == word[word.length-1-i]) {
            count += 1;
        }
        
    }

    if (count == word.length) {
        p_word = "a palindrome.";
    } else {
        p_word = "not a palindrome.";
    }
    return p_word;
}

function main() {
    let word = String(prompt("Enter a word(Check if its a palindrome): "));
    let p_word = palindrome(word);
    console.log(`The word is ${p_word}`);
}

main()