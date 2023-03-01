# class dog():
#     species = 'mammal'#class object attribute (like constant)

#     def __init__(self,breed,name):
#         self.breed = breed
#         self.name = name

#     #methods starts
#     def bark(self):
#         print(f'Geu Geu Geu!!! My name is {self.name}')




# myDog = dog("Desi","Jonny")
# print(myDog.breed)
# print(myDog.name)

# myDog.bark()


import math
class Circle():
    pi = 3.1416
    def __init__(self,radius=1):
        self.radius = radius
        self.area = pow(radius,2)*self.pi

    def circumference(self):
        print(f'Area is {self.area}')
        return  2*self.pi*self.radius
    

area_calc = Circle(3)
print(area_calc.circumference())