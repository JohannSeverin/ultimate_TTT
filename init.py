import pandas as pd 
import numpy  as np
import os
import runpy
import dill

init_amount = 1000

# Make folder if none
if 'init_data' not in os.listdir():
	os.mkdir("init_data")
else:
	for file in os.listdir("init_data"):
		os.remove('init_data/' + file)


config = """
data_path = 'init_data' 
player1 = "functions/player1_rand.dat"
player2 = "functions/player2_rand.dat"
"""

if "config.py" in os.listdir():
	os.remove("config.py")

file = open("config.py", 'w+')
file.write(config)
file.close()


if "functions" not in os.listdir():
    os.mkdir('functions')


from Johanns_funktioner import Player1, Player2
file = open("functions/player1_rand.dat", 'wb')
byte = dill.dumps(Player1, recurse = True)
dill.dump(byte, file)
file.close()

file = open("functions/player2_rand.dat", 'wb')
byte = dill.dumps(Player2, recurse = True)
dill.dump(byte, file)
file.close()



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

model = LGBMClassifier(max_depth = 5, num_leaves = 64, device = 'gpu', n_classes = 81)

model.fit(np.array(player_vect), np.array(player_label))



from Johanns_funktioner import glob_update, availible_moves

def Player(board, t, won):
    avail = availible_moves(board, t, won)
    
    x = np.concatenate([np.array([board]).ravel(), np.array(t).ravel(), np.array(won).ravel()])
    y = model.predict_proba(x.reshape(1, 91))[0][avail]
    
    choice = np.random.choice(avail, p = y / sum(y))

    return choice // 9, choice % 9


if "lightgbm" not in os.listdir("functions"):
    os.mkdir("functions/lightgbm")


file = open("functions/lightgbm/function000.dat", 'wb')
byte = dill.dumps(Player, recurse = True)
dill.dump(byte, file)
file.close()

config = """
data_path = False
player1 = "functions/lightgbm/function000.dat"
player2 = "functions/lightgbm/function000.dat"
"""

if "config.py" in os.listdir():
	os.remove("config.py")

file = open("config.py", 'w+')
file.write(config)
file.close()


print("Model saved")
print("Initialize complete")

os.system("rm -r init_data/")
