import math


class calculator:
    def __init__(self,number):
        self.number = int(number)
        self.result = self.number**2
        self.result1 = self.number**3
        self.result3 = math.sqrt(self.number)
    
    def getResult(self):
        print(f"The Square of {self.number} is {self.result}")
        print(f"The Cube of {self.number} is {self.result1}")
        print(f"The Square root of {self.number} is {self.result3}")


user = int(input("Enter the number: "))

userCalc = calculator(user)

# userCalc.square(user)

userCalc.getResult()