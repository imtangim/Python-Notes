class emplyee:
    company = "google"
    def __init__(self, name, salary,subunit):   #---> Constructor: it will automatically initialize after the class object has been called
        print("Employe is created")
        self.name =name
        self.salary = salary
        self.subunit = subunit

    def details(self):
        print(f"The name of employe: {self.name} ")
        print(f"The salary of employe: {self.salary} ")
        print(f"The subunit of employe: {self.subunit} ")




    def getsalary(self):
        
        print(f"it's salary time!! Your salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

    
tanjim = emplyee("Tanjim",100,"youtube")
tanjim.salary = "100K"
tanjim.getsalary()   #----> self convert this class attrbute and pass tanjim to get salary ---> employee.getsalary(tanjim) 
tanjim.greet() #---->by using @staticmethod, it usually tell us ---> employee.greet()
tanjim.details()