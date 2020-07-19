rounds = 250

model = "lightgbm_function000.dat"

import os

config = f"""
data_path = None 
player1 = "functions/{model}"
player2 = "functions/player2_rand.dat"
"""


if "config.py" in os.listdir():
    os.remove("config.py")

file = open("config.py", 'w+')
file.write(config)
file.close()


counter = {'0':0, '1':0, '2':0}

for i in range(rounds):
    exec(open("The_Arena.py").read())
print(f"Player1 vs. Random: {counter}")


config = f"""
data_path = None 
player1 = "functions/player1_rand.dat"
player2 = "functions/{model}"
"""


if "config.py" in os.listdir():
    os.remove("config.py")

file = open("config.py", 'w+')
file.write(config)
file.close()

counter = {'0':0, '1':0, '2':0}

for i in range(rounds):
    exec(open("The_Arena.py").read())

print(f"Player2 vs. random: {counter}")



config = f"""
data_path = None 
player1 = "functions/{model}"
player2 = "functions/{model}"
"""


if "config.py" in os.listdir():
    os.remove("config.py")

file = open("config.py", 'w+')
file.write(config)
file.close()

counter = {'0':0, '1':0, '2':0}

for i in range(rounds):
    exec(open("The_Arena.py").read())

print(f"Player1 vs. Player2: {counter}")
