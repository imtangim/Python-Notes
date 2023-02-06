with open('Python\Chapter_9_I_O_File\sample_2.txt', 'r') as f:
    a = f.read()
print(a)
with open('Python\Chapter_9_I_O_File\sample_2.txt', 'w') as f:
    a2 = f.write("Hey Fuckersss!!!!")
print(a)