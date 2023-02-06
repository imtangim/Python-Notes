class employee:
    company = "Camel"
    salary = 100
    location = "Dhaka"


    # def changeSalary(self,sal):
    #     self.__class__.salary = sal   #-----> __class__ changes the employe class attribute not the def of changeSalary

    @classmethod     #-----> same as before
    def changeSalary(cls,sal):
        cls.salary = sal

e = employee()
print(e.salary)
e.changeSalary(3000)
print("salary of e object",e.salary)
print("Salary of Employe class",employee.salary)