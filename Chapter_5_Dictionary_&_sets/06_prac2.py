a = input("enter your sets of number (separated by coma): ")
a_splited = a.split(",")
a_set  = set()
formated_a = {}
i=0
for x in a_splited:
    formated_a[i] = int(a_splited[i])
    a_set.add(formated_a[i])
    i+=1

print("Your set is----> ",a_set)
