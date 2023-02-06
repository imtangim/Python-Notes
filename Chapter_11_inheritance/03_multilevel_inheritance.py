# Parent Class ==> Child 1 ==> Child 2 ==> Child 3 .......


class person:
    country = "India"
    def takeBreath(self):
        print("i'm breathing......")
class employee(person):
    company = "honda"
    def getSalary(self):
        print(f"salary is {self.salary}")
    def takeBreath(self):
        print("i'm breathing and employe.....")


class programmer(employee):
    company = "Fiver"
    def getSalary(self):
        print("No salary to programmers")
    def takeBreath(self):
        print("i'm breathing and Programmer++.....")


p = person()
p.takeBreath()

e = employee()
e.takeBreath()
pr = programmer()
pr.takeBreath()
print(pr.country)