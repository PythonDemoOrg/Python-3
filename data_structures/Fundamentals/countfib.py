"""
File: countfib.py
Prints the number of calls of a recursive Fibonacci
function with problem that double.
"""
from counter import Counter

def fib(n, counter):
    """Count the number of calls of the Fibonacci
    function."""
    counter.increment()
    if n < 3:
        return 1
    else:
        return fib(n-1, counter) + fib(n-2, counter)

problemSize = 2

print("%12s%16s" % ("Problem Size", "Calls"))
for count in range(5):
    counter = Counter()

    # The start of the algorithm
    fib(problemSize, counter)
    # The end of the algorithm

    print("%12d%16.3f" % (problemSize, counter))
    problemSize *= 2