iterations = 10
initialize = False
trim_files = True


# Run init
import os
if initialize:
    print("Starting initialization")
    os.system("rm -rf functions")
    exec(open("init.py").read())
    print('initialization complete')

import numpy as np
for iteration in range(iterations):
    if "data" in os.listdir() and trim_files:
        files = np.array(os.listdir("data"))
        choice = np.random.randint(2, size = len(files)).astype(bool)
        files = files[choice]
        for file in files:
            os.remove("data/" + file)

    print("Starting next iteration")
    exec(open("iterate.py").read())

    print("Testing newest iteration")
    exec(open("test_vs_random.py").read())

