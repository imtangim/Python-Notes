class emplyee:
    company = "google"
    def getsalary(self):
        print(f"it's salary time!! Your salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

    
tanjim = emplyee()
tanjim.salary = "100K"
tanjim.getsalary()   #----> self convert this class attrbute and pass tanjim to get salary ---> employee.getsalary(tanjim) 
tanjim.greet() #---->by using @staticmethod, it usually tell us ---> employee.greet()