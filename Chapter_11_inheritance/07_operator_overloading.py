
class number:
    def __init__(self,num):
        self.num=num
    def __add__(self,num2):
        print("Let's add")
        return self.num+num2.num
    def __mul__(self,num2):
        print("Let's add")
        return self.num*num2.num

n1 = number(4)
n2 = number(5)
sum = n1+n2
mul= n1*n2
print(sum)
print(mul)