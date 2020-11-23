#tic tac toe
#p1 = x
#p2 = O

# no chosen out of range


row1 = ["   ", "   ", "   "]
row2 = ["   ", "   ", "   "]
row3 = ["   ", "   ", "   "]

def print_grid():
    print(row1)
    print(row2)
    print(row3)

      

moves_made = []
  

def p1move(p1row,p1column):
    if p1row == 1 :
        row1[p1column - 1] = " x "
    elif p1row == 2 :
        row2[p1column - 1] = " x "
    elif p1row == 3 :
        row3[p1column - 1] = " x "

def p2move(p2row,p2column):
    if p2row == 1 :
        row1[p2column - 1] = " O "
    elif p2row == 2 :
        row2[p2column - 1] = " O "
    elif p2row == 3 :
        row3[p2column - 1] = " O "



#to win
def check(row1,row2,row3):
    if (row1[0] == row1[1] == row1[2] or row1[0] == row2[0] == row3[0] or row1[0] == row2[1] == row3[2]):
        if row1[0] == " x " :
            print("Player 1 is the winner!")
            return True
        elif row1[0] == " O ":
            print("Player 2 is the winner!")
            return True
        
    elif (row1[1] == row2[1] == row3[1]):
        if row1[1] == " x " :
            print("Player 1 is the winner!")
            return True
        elif row1[1] == " O ":
            print("Player 2 is the winner!")
            return True
        
    elif (row1[2] == row2[1] == row3[0] or row1[2] == row2[2] == row3[2]):
        if row1[2] == " x " :
            print("Player 1 is the winner!")
            return True
        elif row1[2] == " O ":
            print("Player 2 is the winner!")
            return True
        
    elif (row2[0] == row2[1] == row2[2]):
        if row2[0] == " x " :
            print("Player 1 is the winner!")
            return  True
        elif row2[0] == " O " :
            print("Player 2 is the winner!")
            return True
        
    elif (row3[0] == row3[1] == row3[2]):
        if row3[0] == " x " :
            print("Player 1 is the winner!")
            return True
        elif row3[0] == " O ":
            print("Player 2 is the winner!")
            return True
        
    return False

win = False
while (win == False):
    p1row = int(input("Player 1 choose your row: "))
    p1column = int(input("Player 1 choose your column: "))
    a = [p1row,p1column]
    if a in moves_made:
        print ("Box taken, choose another box")
    else:
        moves_made.append(a)
        p1move(p1row, p1column)
        print_grid()

        if check(row1,row2,row3) == True :
            win = True

        elif len(moves_made) == 9 and win == False:
            print ("Tie!")
            break

        loop = True
        if win == False :
            while loop == True :
                p2row = int(input("Player 2 choose your row: "))
                p2column = int(input("Player 2 choose your column: "))
                b = [p2row,p2column]
                
                if b in moves_made:
                    print ("Choose another box")
                    loop = True
                else:
                    moves_made.append(b)
                    p2move(p2row, p2column)
                    print_grid()
                    loop = False
                    if check(row1,row2,row3) == True:
                        win = True













