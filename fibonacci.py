""" Recursion Example """
'''
def fib(n):
  if n <= 1:
    return n
  t = fib(n-1) +fib(n-2)
  return t
'''
# Note: This is a particularly inefficient algorithm, and we will show one way of fixing it when we learn about dictionaries:

# Efficient way with dictionaries:

""" 
If yor draw graph of function call some function frames (instances when the function has been invoked), with lines connecting each frame to the frames of the functions it calls. At the top of the graph, fib with n = 4 calls fib with n = 3 and n = 2. In turn, fib with n = 3 calls fib with n = 2 and n = 1. And so on.

Count how many times fib(0) and fib(1) are called. This is an inefficient solution to the problem, and it gets far worse as the argument gets bigger.

A good solution is to keep track of values that have already been computed by storing them in a dictionary. A previously computed value that is stored for later use is called a memo. Here is an implementation of fib using memos:
"""

alreadyknown = {0: 0, 1: 1}
def fib(n):
    if n not in alreadyknown:
        new_value = fib(n-1) + fib(n-2)
        alreadyknown[n] = new_value
    return alreadyknown[n]

"""
The dictionary named alreadyknown keeps track of the Fibonacci numbers we already know. We start with only two pairs: 0 maps to 1; and 1 maps to 1.

Whenever fib is called, it checks the dictionary to determine if it contains the result. If it’s there, the function can return immediately without making any more recursive calls. If not, it has to compute the new value. The new value is added to the dictionary before the function returns.
"""
	
import time
n = 40
t0 = time.clock()
result = fib(n)
t1 = time.clock()
print("fib({0}) = {1}, ({2:.2f} secs)".format(n, result, t1-t0))  
