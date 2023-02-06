b = set()
print(type(b))
b.add(4)
b.add(5)
b.add((3,4,5,7,8))  #--> list and dictionary cant be included in set but tuple can. Because both are unhasble(mutable) type.



# print(len(b))



# ---- Removing something from set -----
b.remove(5)
print(b)


#----removing a randaom from set-----
print(b.pop())


