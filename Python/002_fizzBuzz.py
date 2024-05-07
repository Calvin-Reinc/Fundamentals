# Task 3: Implement a program that takes a numeric input from the user and 
# prints all numbers from 1 to that number. However, for multiples of three, 
# print "Fizz" instead of the number, and for the multiples of five, print "Buzz". 
# For numbers which are multiples of both three and five, print "FizzBuzz".

def fizzBuzz(number):

    for i in range(1, number+1):
        if i % 3 == 0 and i % 5 == 0 :
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")                                           
        else:
            print(i)


if __name__ == "__main__":
    myBool = True
    while myBool:
        try:
            userNumber = int(input("Enter a number: "))
            myBool = False
        except:
            print("An error occured")
    fizzBuzz(userNumber)