from datetime import datetime, date
table= [['- ','- ','- '],['- ','- ','- '],['- ','- ','- ']]


def score(result):
    date = datetime.today()
    if(result == 'x' or result == 'o'):
        with open("Python\\Udemy\\Project\\Score.txt","a") as f:
                score = f.write(f'Player {result.upper()} is winner---->'+ str(date.hour)+str(date.minute)+"\n")
    else:
        with open("Python\\Udemy\\Project\\Score.txt","a") as f:
                score = f.write(f'Match Drawn---->'+ str(date.hour)+str(date.minute)+"\n")

def display_score():
    import os    

    if os.path.getsize('Python\\Udemy\\Project\\Score.txt') == 0:
        print("No Game has been played")
    else:
        with open("Python\\Udemy\\Project\\Score.txt", "r") as f:
            score = f.read()
            line = f.readline()
            print(score)    
    print()
    user_int()

def gameX(column,row):
    table[column][row] = 'x '
    return table[column][row]

def gameO(column,row):
    table[column][row] = 'o '
    return table[column][row]

def result():
    if(table[0][0] == 'x ' and table[0][1] == 'x ' and table[0][2] == 'x '):
        return 1
    elif(table[1][0] == 'x ' and table[1][1] == 'x ' and table[1][2] == 'x '):
        return 1
    elif(table[2][0] == 'x ' and table[2][1] == 'x ' and table[2][2] == 'x '):
        return 1

    elif(table[0][0] == 'x ' and table[1][0] == 'x ' and table[2][0] == 'x '):
        return 1
    elif(table[0][1] == 'x ' and table[1][1] == 'x ' and table[2][1] == 'x '):
        return 1
    elif(table[0][2] == 'x ' and table[1][2] == 'x ' and table[2][2] == 'x '):
        return 1

    elif(table[0][0] == 'x ' and table[1][1] == 'x ' and table[2][2] == 'x '):
        return 1
    elif(table[0][2] == 'x ' and table[1][1] == 'x ' and table[2][0] == 'x '):
        return 1
   


    elif(table[0][0] == 'o ' and table[0][1] == 'o ' and table[0][2] == 'o '):
        return 0
    elif(table[1][0] == 'o ' and table[1][1] == 'o ' and table[1][2] == 'o '):
        return 0
    elif(table[2][0] == 'o ' and table[2][1] == 'o ' and table[2][2] == 'o '):
        return 0

    elif(table[0][0] == 'o ' and table[1][0] == 'o ' and table[2][0] == 'o '):
        return 0
    elif(table[0][1] == 'o ' and table[1][1] == 'o ' and table[2][1] == 'o '):
        return 0
    elif(table[0][2] == 'o ' and table[1][2] == 'o ' and table[2][2] == 'o '):
        return 0

    elif(table[0][0] == 'o ' and table[1][1] == 'o ' and table[2][2] == 'o '):
        return 0
    elif(table[0][2] == 'o ' and table[1][1] == 'o ' and table[2][0] == 'o '):
        return 0
    
    else:
        return 2


def start_game():

    for i in range(9):
        print("You CAN ANYTIME BY ENTERING ANYKEY")
        try:
            column,row = input("Enter the cordination For 'Player x ' Ex. column,row : ").split()
            column = int(column)
            row = int(row)
            display = gameX(column,row)
            for i in table:
                for j in i:
                    print(j, end="")
                print()
            print()
            res = result()
            if(res == 1):
                score("x")
                print("Player x  has won")
                break


            column2,row2 = input("Enter the cordination For 'Player Y' Ex. column,row : ").split()
            column2 = int(column2)
            row2 = int(row2)
            display = gameO(column2,row2)
            for i in table:
                for j in i:
                    print(j, end="")
                print()
            print()
            res = result()
            if(res == 0):
                score("o")
                print("Player o  has won")
                break
        except:
            print()
            user_int()

        
def user_int():
    print("'Press R' to start\n'Press S' for score\n'Press Q' to quite" )
    user = input().lower()
    if(user == 's'):
        display_score()
    elif(user == 'r'):
        start_game()
    elif(user == 'q'):
        quit()
    else:
        print("Enter Correct Keyword")
        user_int()

user_int()