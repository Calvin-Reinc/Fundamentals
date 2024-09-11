# 5. Object-Oriented Programming
# Task 8: Define a class named Rectangle that can be used to create 
# rectangle objects. Include an initializer, properties for width and 
# height, and a method to calculate the area of the rectangle. 
# Create several rectangle objects, calculate their area, and 
# print the results.
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def rectangles(self):
        for y in range(self.height): # controls columns
            print("*"*self.width)
            
    def area(self):
        area = int(self.height * (self.width))
        print(f"The area of the rectangle is {str(area)}")
            

if __name__ == "__main__":
    value1 = int(input("enter width: "))
    value2 = int(input("enter height: "))
    myRect = Rectangle(value1, value2)
    myRect.rectangles()
    myRect.area()

