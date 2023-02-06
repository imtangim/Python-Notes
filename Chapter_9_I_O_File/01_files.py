# f = open('Python\Chapter_9_I_O_File\sample.txt','r')
f = open('Python\Chapter_9_I_O_File\sample.txt')  #--->by default the mode is 'r' means read
# data = f.read()
data = f.read(100) #--->reading first 100 character as it has assign to read 100 character
print(data)
f.close()