def sumofn(n):
    if n>0:
        return n+sumofn(n-1)
    else:
        return 0


print(sumofn(4))