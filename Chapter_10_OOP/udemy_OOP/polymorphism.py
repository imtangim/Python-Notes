class Dog():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + " say Woof"
    
class Cat():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + " says Meu"
    
niko = Dog("Niko")
push = Cat("Push")

# print(niko.speak())
# print(push.speak())

for pet_class in [niko,push]:
    print(type(pet_class))
    print(pet_class.speak())

def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)



