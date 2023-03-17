def namota(x):
    for i in range (0,x):
        for j in range(0,11):
            steps= i * j
            print(f'{i} x {j} = {steps}')
        print(f'namota of {i} is printed')
            

x = int(input("enter the value = "))

namota(x)
