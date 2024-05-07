# Task 2: Write a program that asks the user to enter a number. 
# Check if the number is even or odd. Then, print an appropriate message to the user.

def odds(number):
     if number % 2 == 0:
       print("That's an even number.")
     else:
       print("That's an odd number.")

if __name__ == "__main__":

    myBool = True
    while myBool:
        try:
            userNumber = int(input("Enter a number: "))
            myBool = False
        except:
            print("An error occured")
    odds(userNumber)

