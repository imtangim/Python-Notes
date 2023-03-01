class Animal():
    def __init__(self,name):
        self.name =name
    def speak(self):
        raise NotImplementedError("Sub Class Must implement this abstract method")
    
class Dog(Animal):
    def speak(self):
        return self.name + " Wof!!"
class Cat(Animal):
    def speak(self):
        return self.name + " Meu!!"
    

myanimal = Cat("Tanjim")
print(myanimal.speak())

youranimal = Dog("Jerin")
print(youranimal.speak())
