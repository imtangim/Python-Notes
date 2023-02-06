# a =12
# b=34

# print("the sum of a and b", a+b)

class Employee:   #--->classs
    company = "google"


harry = Employee()  #--->object

rajni = Employee()

harry.company = "youtube"  #-->class attribute
rajni.company = "Pornhub"

harry.sleep = "yes"   #-->instance attribute
rajni.sleep = "no"

print(harry.company)
print(rajni.company)
print(harry.sleep)
print(rajni.sleep)