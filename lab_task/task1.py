def rev(tupl):
    new_list = list(tupl)
    # print(type(new_list))
    new_list.reverse()
    return tuple(new_list)

tup = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')

tup_new = rev(tup)

for i in tup_new:
    print(i)

