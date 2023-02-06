


class person:
    country = "India"
    def __init__(self):
        print("Initializing Person.......\n")


    def takeBreath(self):
        print("i'm breathing......")
class employee(person):
    company = "honda"
    def __init__(self):
        super().__init__()
        print("Initializing Employe.......\n")
    def getSalary(self):
        print(f"salary is {self.salary}")
    def takeBreath(self):
        super().takeBreath()
        print("i'm breathing and employe.....")


class programmer(employee):
    company = "Fiver"
    def __init__(self):
        super().__init__()
        print("Initializing Programmer.......\n")
    def getSalary(self):
        print("No salary to programmers")
    def takeBreath(self):
        super().takeBreath()   #find this method in its parent class and initialize it
        print("i'm breathing and Programmer++.....")


# p = person()
# p.takeBreath()

# e = employee()
# e.takeBreath()

pr = programmer()
# pr.takeBreath()
# print(pr.country)