# Task 6: Write a function that takes two numbers as arguments and 
# returns their sum, their product, and the difference between the two numbers. 
# Call this function from your main program and print the results.
def mathematics(x, y):
    return x+y, x*y, x-y


if __name__ == "__main__":

    x = int(input("Enter value: "))
    y= int(input("Enter value: "))

    mySum, myProduct, myDifference = mathematics(x, y)
    print(f"The sum of {x} and {y} is {mySum}")
    print(f"The product of {x} and {y} is {myProduct}")
    print(f"The difference of {x} and {y} is {myDifference}")