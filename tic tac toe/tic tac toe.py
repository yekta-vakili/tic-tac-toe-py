from tracemalloc import start
from colorama import Fore
import random
import time

game=[['-' ,'-' ,'-' ],
     ['-' ,'-' ,'-' ],
     ['-' ,'-' ,'-' ]]

gamee=False

print("1-play with computer")
print("2-play with other")
select=int(input())
for row in game:
    for item in row:
        print(item,end=" ")
    print()
start = time.time()

def show_game_board(): 
    for i in range(3): 
        for j in range(3):
            if game[i][j] == "O":                
                print(Fore.RED + "O", end=" ") 
            elif game[i][j] == "X": 
                print(Fore.BLUE + "X", end=" ") 
            else: 
                print(Fore.YELLOW + "-", end=" ") 
        print(Fore.RESET)

def checkg():
    global gamee
    
if(game[0][0]=="X"and game[0][1]=="X" and game[0][2]=="X"):
    print("X win")
       
elif(game[1][0]=="X"and game[1][1]=="X"and game[1][2]=="X"):
    print("X win")
    
elif(game[2][0]=="X" and game[2][1]=="X" and game[2][2]=="X"):
    print("X win")
    
elif(game[0][0]=="X"and game[1][0]=="X"and game[2][0]=="X"):
    print("X win")
    
elif(game[0][1]=="X" and game[1][1]=="X" and game[2][1]=="X"):
    print("X win")
    
elif(game[0][2]=="X" and game[1][2]=="X" and game[2][2]=="X"):
    print("X win")
    
elif(game[0][0]=="X" and game[1][1]=="X" and game[2][2]=="X"):
    print("X win")
    
elif(game[0][2]=="X" and game[1][1]=="X" and game[2][0]=="X"):
    print("X win")
    
if(game[0][0]=="O"and game[0][1]=="O" and game[0][2]=="O"):
    print("O win")
       
elif(game[1][0]=="O"and game[1][1]=="O"and game[1][2]=="O"):
    print("O win")
    
elif(game[2][0]=="O" and game[2][1]=="O" and game[2][2]=="O"):
    print("O win")
    
elif(game[0][0]=="O"and game[1][0]=="O"and game[2][0]=="O"):
    print("O win")
    
elif(game[0][1]=="O" and game[1][1]=="O" and game[2][1]=="O"):
    print("O win")
    
elif(game[0][2]=="O" and game[1][2]=="O" and game[2][2]=="O"):
    print("O win")
    
elif(game[0][0]=="O" and game[1][1]=="O" and game[2][2]=="O"):
    print("O win")
    
elif(game[0][2]=="O" and game[1][1]=="O" and game[2][0]=="O"):
    print("O win")
if((game[0][0]=="X" or game[0][0]=="O") and(game[0][1]=="X" or game[0][1]=="O")
and (game[0][2]=="X" or game[0][2]=="O" ) and(game[1][0]=="X" or game[1][0]=="O")
and (game[1][1]=="X" or game[1][1]=="O") and (game[1][2]=="X" or game[1][2]=="O")
and (game[2][0]=="X" or game[2][0]=="O") and (game[2][1]=="X" or game[2][1]=="O")
and (game[2][2]=="X" or game[2][2]=="O")):
        print("Draw")
        gamee=True
         
        

if select==1:    
    while(not gamee):
        while(True):
          print("Player1")
          row=int(input("row:"))
          col=int(input("col:"))
          if game[row][col]=="-":
             game[row][col]="X"      
             break
          else:
              print("be careful")
        
        show_game_board()
        checkg()  
        while(True):
            print("Player2")
            row=int(input("row:"))
            col=int(input("col:"))
            if game[row][col]=="-":
                game[row][col]="O"
                break
            else:
                print("be careful")
        show_game_board()
        checkg()
elif select==2:
    while(not gamee):
        while(True):
          print("You:")
          row=int(input("row:"))
          col=int(input("col:"))
          if game[row][col]=="-":
             game[row][col]="X"
             break
          else:
              print("be careful")
                   
        show_game_board()        
        checkg()
        if not gamee:
            
           print("Computer:")
           while(True):
              row=random.randint(0,2)
              col=random.randint(0,2)
              if game[row][col]=="-":
                 game[row][col]="O"
                 break
              else:
                row=random.randint(0,2)
                col=random.randint(0,2)

        show_game_board()
        checkg()