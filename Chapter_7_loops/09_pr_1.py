number = int(input("Enter the number: "))

i=1

# while i<11:
#     print(str(number),"*",str(i),"=",int(number*i))
#     i+=1

for i in range(11):
    # print(str(number),"*",str(i),"=",int(number*i))
    print(f"{number}*{i}={number*i}")

