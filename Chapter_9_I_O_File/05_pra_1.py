with open("E:\Workspace\Python\Chapter_9_I_O_File\sample_2.txt","r") as f:
    poem = f.read()
# print(poem.find("star"))

if "twinkle" in poem:
    print("YEAH FUCK YOU")

else:
    print("Nothing")