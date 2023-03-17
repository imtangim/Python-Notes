dic_a = {}
dic_b ={}
dic_c ={}

def upadate_dic(a,b):
    i = 1
    for j in range(a):
        key = input(f'Enter the {i} key of {1} dict: ')
        value =input(f'Enter the {i} key of {1} dict: value: ')
        dic_a.update({key:value})
        i+=1

    k=1
    for j in range(b):
        key = input(f'Enter the {k} key of {1} dict:: ')
        value =input(f'Enter the {k} value of {1} dict:: ')
        dic_b.update({key:value})
        k+=1

def merge():
    dic_c.update(dic_a)
    dic_c.update(dic_b)



a = int(input("How Many key and value you have for first Dictionary : "))
b = int(input("How Many key and value you have for second Dictionary : "))

upadate_dic(a,b)
merge()


print(dic_c)



