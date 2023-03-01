class Animal():  #base class
    def __init__(self):
        print("Animal OOP Created")
    
    def Who_am_i(self):
        print("Im an animal")
    
    def eat(self):
        print("I'm eating")

class Dog(Animal):
    #inherting base class
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
    def Who_am_i(self):
        print("Im a Dog")

        
mydog =Dog()
mydog.Who_am_i()