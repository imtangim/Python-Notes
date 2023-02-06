def factorial_iter(n):
    if n == 1  or n == 0:
        return 1
    else:
        return n*factorial_iter(n-1)


print(factorial_iter(2))