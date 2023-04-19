from os import *
from sys import *
from collections import *
from math import *

def printPascal(n:int):
    # Write your code here.
    # Return a list of lists.
    val = []
    for i in range(n):
        pL = []
        for j in range(i+1):
            sm = choose(i,j)
            pL.append(sm)
        val.append(pL)
    return val

def choose(n,r):
    return int(factorial(n) /(factorial(r) * factorial(n-r)))


ml = printPascal(4)

print(ml)
print(* ml[1])
