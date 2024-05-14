# Task 7: Create a function that checks whether a given word is a palindrome or not.
def palidrome(word):
    count = 0
    for x in range(len(word)):
        # compares the x word with its reverse
        if word[x] == word[len(word)-1-x]:
            count += 1
    if count == len(word):
        p_word = "a palindrome."
    else:
        p_word = "not a palindrome."

    return p_word

if __name__ == "__main__":

    word = str(input("Enter a word(Check if its a palindrome): "))   
    p_word = palidrome(word)
    print(f"The word is {p_word}")