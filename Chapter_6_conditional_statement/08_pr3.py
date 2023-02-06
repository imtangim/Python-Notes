comment = input("Enter the text: ")

if("make a lot of money" in comment or "money" in comment or "Money" in comment):
    spam = True
elif("buy now" in comment):
    spam = True
elif("click this" in comment):
    spam = True
elif("subscribe" in comment):
    spam = True
else:
    spam= False

if(spam == True):
    print("Scam allert!!!!!!!")
else:
    print("Safe")