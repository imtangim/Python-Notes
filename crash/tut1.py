# # print("vatkhabo") commented


# # a = int(input())
# # b = int(input())

# nissan = int(input())
# oni = int(input())
# tangim= int(input())

# def compare(a,b,c):  # with parameter/with argument and without return
#     nissan = a
#     oni = b
#     tangim =c
#     if(oni>nissan):
#         if(oni>tangim):
#             return oni
#         else:
#             return tangim
    
#     else:
#         if(nissan>tangim):
#             return nissan
#         else:
#             return tangim


# result = compare(nissan,oni,tangim)
# print(f'1Highest Number: {result}')
# # result = str(result)
# print("Highest Number: " , result)

import random

def randomnum():
    return random.randint(1,10)


def haramjada():
    print("haramjada vul koresis")
    
a = int(input("Enter a number"))


if((randomnum()*a)!= 4):
    haramjada()

else:
    print(f'{randomnum*a}')







