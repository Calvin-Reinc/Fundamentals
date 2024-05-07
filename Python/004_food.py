# Data Structures
# Task 4: Create a program that asks the user to enter their favorite foods. 
# Store these in a list (or array in JavaScript) and then print them back to the user.
def order():
    
    userFood = str(input("What is your favourite food."))
    foodList = []
    foodList.append(userFood)
    myBool = True

    while myBool:
        userRes = input("Is that all you wanted?Y or N: ")[0]
        if userRes.casefold() == "n":
            userFood = str(input("What is your favourite food."))
            foodList.append(userFood)
            continue
        if userRes == "y":
            myBool = False

    print("This are your favourite food/s.")
    for i in range(len(foodList)):
        print(f"1. {foodList[i]}")




if __name__ == "__main__":
    order()