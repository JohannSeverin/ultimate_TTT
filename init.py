import pandas as pd 
import numpy  as np
import os
import runpy

# Make folder if none
if 'init_data' not in os.listdir():
	os.mkdir("init_data")
else:
	for file in os.listdir("init_data"):
		os.remove('init_data/' + file)


config = """
data_path = 'init_data' 
"""

if "config.py" in os.listdir():
	os.remove("config.py")

file = open("config.py", 'w+')
file.write(config)
file.close()


func_load = """
from Johanns_funktioner import Player1, Player2
"""

if "func_load.py" in os.listdir():
    os.remove("func_load.py")

file = open("func_load.py", 'w+')
file.write(func_load)
file.close()

init_amount = 1000

print(f"Generating initial data: {init_amount} games")

for game in range(init_amount):
    if game / init_amount * 100 % 10 == 0:
        print(f"{game / init_amount * 100}% games done") 
    exec(open("The_Arena.py").read())
    

print("Initial games played")


print("Converting to vector data")

files = os.listdir("init_data")

player_vect = []
player_label = []

for filename in files:
    data = pd.read_pickle('init_data/' + filename)
    if data['winner'] == 1:
        for i in range(len(data['board'])):
            if data['tur'][i] == 1:
                player_vect.append(np.concatenate([np.array(data['board'][i]).ravel(), np.array(data['ts'][i]).ravel(), np.array(data['gl_board'][i]).ravel()]))
                player_label.append(data['move'][i][0] * 9 + data['move'][i][1])
    if data['winner'] == 2:
        for i in range(len(data['board'])):
            if data['tur'][i] == 2:
                player_vect.append(np.concatenate([np.array(data['board'][i]).ravel(), np.array(data['ts'][i]).ravel(), np.array(data['gl_board'][i]).ravel()]))
                player_label.append(data['move'][i][0] * 9 + data['move'][i][1])
    else:
        continue

print("Vector data done")
print("Training initial model")

from lightgbm import LGBMClassifier

model = LGBMClassifier()

model.fit(np.array(player_vect), np.array(player_label))

print("Training done")

if "models" not in os.listdir():
    os.mkdir('models')

pd.to_pickle(model, 'models/model000')

func_load = """
import pandas as pd

model = pd.read_pickle("models/model000")

def glob_update(board):
    glob_board = []
    for i in range(len(board)):
        arr = np.array(board[i]).reshape(3,3)
        ones, twos = arr == 1, arr == 2
        if any(np.sum(ones, axis = 0)) == 3 \
            or any(np.sum(ones, axis = 1) == 3) \
            or np.trace(ones) == 3 \
            or np.trace(np.rot90(ones)) == 3:
            glob_board.append(1)

        elif any(np.sum(twos, axis = 0)) == 3 \
            or any(np.sum(twos, axis = 1) == 3) \
            or np.trace(twos) == 3 \
            or np.trace(np.rot90(twos)) == 3:
            glob_board.append(2)
        else:
            glob_board.append(0)
    return glob_board

def availible_moves(board, t, won):
    # Return all availible moves in a, b format.
    # Return None if no moves are availible

    if t == 9: # Return all availible fields if no board is forced
        moves = []
        for i in range(len(board)):
            if won[i] == 0:
                bs = np.array(board[i]) == 0
                moves.extend([i * 9 + b for b in bs.nonzero()[0]])
        return moves
    else:    # Return field in the forced board
        local = board[t]
        a = t
        bs = np.array(local) == 0
        if np.sum(bs) == 0:
            return None
        else:
            return [a * 9 +  b for b in bs.nonzero()[0]]

def Player(board, t, won):
    avail = availible_moves(board, t, won)
    
    x = np.concatenate([np.array([board]).ravel(), np.array(t).ravel(), np.array(won).ravel()])
    y = model.predict_proba(x.reshape(1, 91))[0][avail]
    
    choice = np.random.choice(avail, p = y / sum(y))

    return choice // 9, choice % 9

Player1 = Player
Player2 = Player
"""

file = open("func_load.py", 'w+')
file.write(func_load)
file.close()

print("Model saved")
print("Initialize complete")


counter = {'0':0, '1':0, '2':0}

exec(open("The_Arena.py").read())

print(counter)