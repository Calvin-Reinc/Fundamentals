# Task 1: Create a program that asks the user for their name and their age, 
# and then calculates the year they will turn 100 years old. Print the result.

def basic():
    
    try:
        userName = input("What's your name? ")
        userAge = int(input("What's your age? "))
        print(f"Hey {userName.capitalize()}, you are {userAge} old.")
    except:
        print('An exception occurred')
    
    return userName


if __name__ == "__main__":
    basic()