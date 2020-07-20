iterations = 15
initialize = False
trim_files = True
shutdown_after = True

import warnings
warnings.filterwarnings("ignore")


# Run init
import os
if initialize:
    print("Starting initialization")
    os.system("rm -rf functions")
    exec(open("init.py").read())
    print('initialization complete')

import numpy as np
for iteration in range(iterations):
    

    print("Starting next iteration")
    exec(open("iterate.py").read())

    print("Testing newest iteration")
    exec(open("test_vs_random.py").read())

    print("Trimming files")
    if "data" in os.listdir() and trim_files:
        files = np.array(os.listdir("data"))
        choice = np.random.randint(2, size = len(files)).astype(bool)
        files = files[choice]
        for file in files:
            os.remove("data/" + file)

if shutdown_after:
    os.system("shutdown now")