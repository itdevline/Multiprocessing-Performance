import random
import time
import multiprocessing

def loopTester(inc):
    for i in range(1, 100000, 1):
        for y in range(1, 100, 1):
            random.random()         # random number generator between 0.1 and 1.0
    print ("End: " , inc)

if __name__ == "__main__":

    begin_timer = time.clock()  # Start timer
    """
    # Serial code
    for x in range(1, 10, 1):
        loopTester(x)
    """
    # multiprocessing code -> parallelizing CPU bound
    procs = []  # Create an empty of list. This list store all process.
    for i in range(1, 10, 1):
        p = multiprocessing.Process(target=loopTester, args=(i,))
        procs.append(p) # Append multiprocessing to list.
        p.start()   # Start the process’s activity. Before we'll start all process then run join.

    for p in procs:
        p.join() # Join -> If we use join, then the main process will be block.

    end_timer = time.clock()    # End timer
    print (end_timer - begin_timer)