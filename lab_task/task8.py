dic_a = {}
def upadate_dic(a):
    i = 1
    for j in range(a):
        key = input(f'Enter the {i} key of {1} dict: ')
        value =input(f'Enter the {i} key of {1} dict: value: ')
        dic_a.update({key:value})
        i+=1


def average(n):
    a = dic_a.values()
    total = 0
    for i in a:
        total = total+int(i)
    return total/n

a = int(input("How Many key and value you have for first Dictionary : "))   
upadate_dic(a)
print(average(a))