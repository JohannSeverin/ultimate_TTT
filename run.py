iterations = 10
initialize = True

# Run init
if initialize:
    print("Starting initialization")
    exec(open("init.py").read())
    print('initialization complete')


for iteration in iterations:
    print("Starting next iteration")
    exec(open("iterate.py").read())

    print("Testing newest iteration")
    exec(open("test_vs_random.py").read())

