import sys
import random as rng
import numpy as np
import pandas as pd
import os
import dill

from config import data_path, player1, player2

byte = dill.load(open(player1, 'rb'))
Player1 = dill.loads(byte)

byte = dill.load(open(player2, 'rb'))
Player2 = dill.loads(byte)

data = {'board': [],
        'gl_board': [],
        'ts':    [],
        'move':  [],
        'tur':   [],
        'winner': 0}

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




while winner == 0:
    data['board'].append(board)
    data['ts'].append(T)
    data['gl_board'].append(won)
    data['tur'].append(tur)
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
    data['move'].append((a, b))
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
        # print('TIE')
        # print(board)
        # sys.exit()
        break
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
    data['winner'] = winner
    if data_path:
        pd.to_pickle(data, data_path + "/game{:06d}".format(len(os.listdir(data_path)) + 1))

if 'counter' in dir():
    counter[str(winner)] += 1

    # print(len(os.listdir('data')))
    # sys.exit()
    # print(f'AND THE WINNER IS ......... PLAYER {winner}')
    # print(board)




