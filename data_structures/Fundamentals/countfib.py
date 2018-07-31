"""
File: countfib.py
Prints the running times for problem sizes that double,
using a single loop.
"""

problemSize = 1000
print("%12s%16s" % ("Problem Size", "Iterations"))
for count in range(5):
    number = 0
    # The start of the algorithm
    work = 1
    for j in range(problemSize):
        for x in range(problemSize):
            number += 1
            work += 1
            work -= 1
    # The end of the algorithm

    print("%12d%16.3f" % (problemSize, number))
    problemSize *= 2