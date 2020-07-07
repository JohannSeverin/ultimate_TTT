import sys
import random as rng
import numpy as np


board = [] 
won = []
winner = 0
T = 9
tur = 1

### Laver bordet
for i in range(9):
    board.append([])
    won.append(0)
for i in range(9):
    for j in range(9):
        board[i].append(0)
# Du kan enten bruge numpy array med np.zeros for at gøre det hurtigere eller
# det er muligt at skrive board = [[0] * 9] * 9, for at få samme resultat. 
# (Har prøvet dette men giver vildt mærkelige resultater som jeg ikke kan få til at give mening.
# det gør at player 1 tager et træk på alle bordene på samme tid.)



# Skriv lidt dokumentation, hvad skal til B og t være ;)
# def Player1(B, t):
#     if t == 9:
#         for i in range(9):
#             if won[i] == 0 and any((True for x in B[i] if x == 0)) == True:
#                 a = i
#                 break
#     else:
#         a = t
#     b = B[a].index(0)
#     return a,b

# def Player2(B,t):
#     if t == 9:
#         list = []
#         for i in range(9):
#             if won[i] == 0 and any((True for x in B[i] if x == 0)) == True:
#                 list.append(i)
#         a = rng.choice(list)
#     else:
#         a = t
#     list =[]
#     for i in range(9):
#         if B[a][i] == 0:
#             list.append(i)
#     b = rng.choice(list)
#     return a,b

from Johanns_funktioner import Player1, Player2 # De to funktioner fra player_generation importeres

while winner == 0:
    if tur ==1:
        a,b = Player1(board,T, won)
    elif tur == 2:
        a,b = Player2(board,T, won)
    if T !=9: ## tjekker om det er et gyldigt træk. Et træk kan være ugyldigt hvis, det ikke er på det tvungne local board, feltet allerede er taget eller local boardet er vundet.
        if a != T:
            print(f'Player{tur} snyder')
            sys.exit()
    if board[a][b] != 0:
        print(f'Player{tur} prøver at tage et taget felt')
        sys.exit()
    if won[a] != 0:
        print(f'Player{tur} prøver at tage på et vundet mini spil')
        sys.exit()
    board[a][b] = tur # Trækket tages
    ### Tjekker om der er nogen der har vundet på mini borene 
    for i in range(9):
        if won[i] == 0:
            # Tjekker om der er nogen spil der er blevet uafgjort og sætter dem til 3 i won listen.
            if any((True for x in board[i] if x == 0)) == False:
                won[i] = 3
            for j in range(3):
                if [board[i][j*3],board[i][j*3+1],board[i][j*3+2]] == [1,1,1]:
                    won[i] = 1
                    break
                elif [board[i][j*3],board[i][j*3+1],board[i][j*3+2]] == [2,2,2]:
                    won[i] = 2
                    break
                elif [board[i][j],board[i][j+3],board[i][j+6]] == [1,1,1]:
                    won[i] = 1
                    break
                elif [board[i][j],board[i][j+3],board[i][j+6]] == [2,2,2]:
                    won[i] = 2
                    break
            if [board[i][0],board[i][4],board[i][8]] == [1,1,1]:
                    won[i] = 1
                    break
            elif [board[i][0],board[i][4],board[i][8]] == [2,2,2]:
                    won[i] = 2
                    break
            elif [board[i][2],board[i][4],board[i][6]] == [1,1,1]:
                    won[i] = 1
                    break
            elif [board[i][2],board[i][4],board[i][6]] == [2,2,2]:
                    won[i] = 2
                    break
    ## Tjekker om der er nogen der har vundet hele spillet.
    for j in range(3):
        if [won[j*3],won[j*3+1],won[j*3+2]] == [1,1,1]:
            winner = 1
            break
        elif [won[j*3],won[j*3+1],won[j*3+2]] == [2,2,2]:
            winner = 2
            break
        elif [won[j],won[j+3],won[j+6]] == [1,1,1]:
            winner = 1
            break
        elif [won[j],won[j+3],won[j+6]] == [2,2,2]:
            winner = 2
            break
    if [won[0],won[4],won[8]] == [1,1,1]:
        winner = 1
    elif [won[0],won[4],won[8]] == [2,2,2]:
        winner = 2
    elif [won[2],won[4],won[6]] == [1,1,1]:
        winner = 1
    elif [won[2],won[4],won[6]] == [2,2,2]:
        winner = 2
    if any((True for x in won if x == 0)) == False:
        print('TIE')
        print(board)
        sys.exit()
    ## Opdatere hvad det tvungne local board er
    if won[b] != 0 or any((True for x in board[b] if x == 0)) == False: # bestemmer hvad det tvungne local board er, hvis local boardet er vundet eller uafgjort bliver T=9 hvilket svare til fri.
        T = 9
    elif won[b] == 0:
        T = b
    ## Opdatere hvis tur det er
    if tur ==1:
        tur = 2
    elif tur == 2:
        tur = 1

        
if winner != 0:
    print(f'AND THE WINNER IS ......... PLAYER {winner}')
    print(board)




