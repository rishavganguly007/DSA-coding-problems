#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'journeyToMoon' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY astronaut
#

def journeyToMoon(n, astronaut):
    # Write your code here
    adj = [[] for _ in range(n)]
    
    for n1, n2 in astronaut:
        adj[n1].append(n2)
        adj[n2].append(n1)
    
    vis = set()
    cntSet = []
    value = 0
    ans = 0
    prev_val = 0
    
    def dfs(s):
        nonlocal value
        vis.add(s)
        for i in adj[s]:
            if i not in vis:
                dfs(i)
        value += 1
    
    for i in range(n) :
        if i not in vis:
            dfs(i)
            
            ans = ans + (prev_val) * value
            prev_val = prev_val + value
            value = 0
    return ans

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    p = int(first_multiple_input[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()
