f = open('Python\Chapter_9_I_O_File\sample.txt','r')

# read line till first new line
data = f.readline()
print(data)

# read line till second new line
data = f.readline()
print(data)


# read line till third new line
data = f.readline()
print(data)
f.close()