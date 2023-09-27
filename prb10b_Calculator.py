import math
# power can also be written as **
# 4**2 = 4*4
class Calculator:
    def __init__(self):
        self.number=int(input("Enter any number="))
    
    @staticmethod
    def greed():
        print("hi")

    def square(self):
        return self.number*self.number
    def cube(self):
        return self.square()*self.number
    def squareRoot(self):
        return math.sqrt(self.number)

calc=Calculator()
print("Square=",calc.square())
print("Cube=",calc.cube())
print("Square Root=",calc.squareRoot())
calc.greed()