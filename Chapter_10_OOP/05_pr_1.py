class programmer:
    def __init__(self,name,unit,salary):
        
        self.name = name
        self.salary = salary
        self.unit = unit
        # print("update has been made")

    
    # def details(self,name,unit,salary):
    #     self.name = name
    #     self.salary = salary
    #     self.unit = unit

    def getDetail(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Unit: {self.unit}")

    
user = input("Enter the Name: ")
salary = input("Enter the Salary: ")
unit = input("Enter the Unit: ")

userObject = programmer(user,unit,salary)
# userObject.details(user,unit,salary)
userObject.getDetail()