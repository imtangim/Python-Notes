# i=0
# j=3
# while j>0:
#     print(" "*(j),"* " * (2*i+1))
#     print(" "*(j))
#     j-=1
#     i+=1

#     # print("*" * (i))

''' 
   *   
  ***
 *****
*******
'''

n=4
for i in range(4):
    print(" "*(n-i-1),end="")
    print("*"*(2*i+1),end="")
    print((" ")*(n-i-1))


'''
* * * 
*   *
* * *
'''
n=3
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print("* ", end="")
        else:
            print("  ",end="")

    print()
