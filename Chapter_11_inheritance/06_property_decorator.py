class employee:
    company = "Bangladesh Officials"
    salary = 10
    salaryBonus = 2
    
    @property
    def totalSalary(self):
        return self.salary+self.salaryBonus

    @totalSalary.setter
    def totalSalary(self,val):
        self.salaryBonus = val - self.salary

e = employee()

print(e.totalSalary)
e.totalSalary = 900
print(e.salary)
print(e.salaryBonus)