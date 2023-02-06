# single inheritance

#-----> single inheritance : parent class ==> child class ==> end


class employee:
    comapny = "Google"
    def showdetails(self):
        print("This is an employe")


class programmer(employee):
    language = "python"
    def getName(self):
        print(f"The language is {self.language}")
    def showdetails(self):    #--->overiding - declare it's own function or attribute though it parent class has the same thing
        print("This is an employe P")

e = employee()
e.showdetails()

p= programmer()
p.showdetails()
print(p.comapny)
