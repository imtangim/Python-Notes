import random
import datetime

def tie_o(user, comp):
    if comp != user:
        if user == 1 and comp == 2 :
            return 1
        elif user == 1 and comp == 3 :
            return 2


        elif user == 2 and comp == 1 :
            return 2
        elif user == 2 and comp == 3 :
            return 1

    
        elif user == 3 and comp == 1 :
            return 1
        elif user == 3 and comp == 2 :
            return 2


    else:
        user1 = int(input("IT'S A TIE. Enter Again Your Number Player(1): "))
        user2 = int(input(" Enter Again Your Number Player(2): "))
        return tie_o(user1,user2)



def tie(user, comp):
    if comp != user:
        if user == 1 and comp == 2 :
            return 1
        elif user == 1 and comp == 3 :
            return 2


        elif user == 2 and comp == 1 :
            return 2
        elif user == 2 and comp == 3 :
            return 1

    
        elif user == 3 and comp == 1 :
            return 1
        elif user == 3 and comp == 2 :
            return 2


    else:
        comp =random.randint(1,3)
        user = int(input("IT'S A TIE. Enter Again Your Number: "))
        return tie(comp,user)
        

def result(user,comp):
    

    if user == 1 and comp == 2 :
        return 1
    elif user == 1 and comp == 3 :
        return 2


    elif user == 2 and comp == 1 :
        return 2
    elif user == 2 and comp == 3 :
        return 1

    
    elif user == 3 and comp == 1 :
        return 1
    elif user == 3 and comp == 2 :
        return 2

    else:
        return 3


print("Press C: Play with Computer")
print("Press O: Play Offline")
print("Press S: See Score")
user =  input().capitalize()


if user == "C":
    comp =random.randint(1,3)
    user = int(input("Select:\nPress(1) for Snake \nPress(2) for Gun\nPress(3) for Water"))
    if result(user,comp) == 1:
        print("Computer have won")
    elif result(user,comp) == 2:
        print("User have won")
    else:
        comp =random.randint(1,3)
        user = int(input("IT'S A TIE. Enter Again Your Number: "))
        tiebreaker = tie(user,comp)
        if tiebreaker == 1:
            print("Computer have won")
        else:
            print("User have won")

 
elif user == "O":
    user1 = int(input("Select Player(1):\nPress(1) for Snake \nPress(2) for Gun\nPress(3) for Water\n"))
    user2 = int(input("Select Player(2):\nPress(1) for Snake \nPress(2) for Gun\nPress(3) for Water\n"))
    if result(user1,user2) == 1:
        print("Player(2) have won")
        with open("Python\\Chapter_Project\\Score.txt","a") as f:
            score = f.write("Player(2) is winner---->"+ str(datetime.datetime.now())+"\n")


    elif result(user1,user2) == 2:
        print("Player(1) have won")
        with open("Python\\Chapter_Project\\Score.txt","a") as f:
            score = f.write("Player(1) is winner---->"+ str(datetime.datetime.now())+"\n")
        
    else:
        user1 = int(input("IT'S A TIE.\nEnter Again Your Number - Player(1): "))
        user1 = int(input("Enter Again Your Number - Player(2): "))
        tiebreaker = tie_o(user1,user2)
        if tiebreaker == 1:
            print("Player(2) have won")
            with open("Python\\Chapter_Project\\Score.txt","a") as f:
                score = f.write("Player(2) is winner---->"+ str(datetime.datetime.now())+"\n")
        elif tiebreaker == 2:
            print("Player(1) have have won")
            with open("Python\\Chapter_Project\\Score.txt","a") as f:
                score = f.write("Player(1) is winner---->"+ str(datetime.datetime.now())+"\n")
        else:
            print("!!!!One of you cheated!!!!\n--->Game dissmissed<---")
            with open("Python\\Chapter_Project\\Score.txt","a") as f:
                score = f.write("Someone has cheated---->"+ str(datetime.datetime.now())+"\n")


elif user == "S":
    with open("Python\\Chapter_Project\\Score.txt","r") as f:
        score = f.read()
    print(score)

    print("Press E to Exit")
    print("Press R to save and exit")
    user=input().capitalize()

    if user == "E":
        exit()
    elif user == "R":
        with open("Python\\Chapter_Project\\Score.txt","w") as f:
            clean = f.write("")
        exit()

    else:
        exit()
        

else:
    print("Enter the correct value")


