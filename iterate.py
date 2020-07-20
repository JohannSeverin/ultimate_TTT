import pandas as pd 
import numpy  as np
import os
import runpy
import dill

amount = 1000

models = os.listdir("functions/lightgbm")
models.sort()

model_num = len(models)

filepath = models[-1]

print(f"Loading model {filepath}")

config = f"""
data_path = 'data' 
player1 = "functions/lightgbm/{filepath}"
player2 = "functions/lightgbm/{filepath}"
"""

if "config.py" in os.listdir():
	os.remove("config.py")

file = open("config.py", 'w+')
file.write(config)
file.close()


for game in range(amount // 2):
    if game / amount * 100 % 10 == 0:
        print(f"{game / amount * 100}% games done") 
    exec(open("The_Arena.py").read())


config = f"""
data_path = 'data' 
player1 = "functions/lightgbm/{filepath}"
player2 = "functions/player2_rand.dat"
"""

if "config.py" in os.listdir():
	os.remove("config.py")

file = open("config.py", 'w+')
file.write(config)
file.close()

for game in range(amount // 2, amount // 4 * 3):
    if game / amount * 100 % 10 == 0:
        print(f"{game / amount * 100}% games done") 
    exec(open("The_Arena.py").read())


config = f"""
data_path = 'data' 
player1 = "functions/player1_rand.dat"
player2 = "functions/lightgbm/{filepath}"
"""

if "config.py" in os.listdir():
	os.remove("config.py")

file = open("config.py", 'w+')
file.write(config)
file.close()


for game in range(amount // 4 * 3, amount):
    if game / amount * 100 % 10 == 0:
        print(f"{game / amount * 100}% games done") 
    exec(open("The_Arena.py").read())




files = os.listdir("data")

player_vect = []
player_label = []

for filename in files:
    data = pd.read_pickle('data/' + filename)
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

print(f"Training model: {model_num}")

from lightgbm import LGBMClassifier

valid_values = set(player_label)
valid_values = list(valid_values)
valid_values.sort()

model = LGBMClassifier(max_depth = 5, num_leaves = 30, device = 'gpu')

model.fit(np.array(player_vect), np.array(player_label))

print("Training done")

if "models" not in os.listdir():
    os.mkdir('models')


pd.to_pickle(model, 'models/model000')

from Johanns_funktioner import glob_update, availible_moves

def Player(board, t, won):
    avail = availible_moves(board, t, won)
    

    x = np.concatenate([np.array([board]).ravel(), np.array(t).ravel(), np.array(won).ravel()])
    y = model.predict_proba(x.reshape(1, 91))[0]

    prob_array = np.zeros(81)
    prob_array[np.array(valid_values)] = y
    prob_array = prob_array[avail]
    if sum(prob_array) != 0:
        try:
            choice = np.random.choice(avail, p = prob_array / sum(prob_array))
        except:
            choice = np.random.choice(avail)
    else:
        choice = np.random.choice(avail)    
    return choice // 9, choice % 9



file = open(f"functions/lightgbm/function{model_num:03d}.dat", 'wb')
byte = dill.dumps(Player, recurse = True)
dill.dump(byte, file)
file.close()

# os.system("rm -r data/")

