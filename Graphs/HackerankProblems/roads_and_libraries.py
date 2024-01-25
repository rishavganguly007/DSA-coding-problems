# code : https://www.hackerrank.com/challenges/torque-and-development/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#

def roadsAndLibraries(n, c_lib, c_road, cities):
    # Write your code here
    if c_road > c_lib:
        return c_lib * n # libraries in each city
        
    adj = [[] for _ in range(n+1)]
    for node1, node2 in cities:
        adj[node1].append(node2)
        adj[node2].append(node1)
        
    vis = [False] * (n+1)
    vis[1] = True
    nodeCount=0
    
    cost = c_lib
    
    
    def dfs(node):
        nonlocal nodeCount
        vis[node] = True
        nodeCount += 1
        for i in adj[node]:
            if vis[i] is False:
                dfs(i)
    
    dfs(1)
    cost = cost + (nodeCount-1) * c_road
    for i in range(2, n+1):
        if not vis[i]:
            nodeCount = 0
            dfs(i)
            cost += c_lib + (nodeCount - 1)*c_road
    return cost


def roadsAndLibraries_OPTIMISED(n, c_lib, c_road, cities):
    # Write your code here
    if c_road > c_lib:
        return c_lib * n  # libraries in each city

    adj = {i: [] for i in range(1, n + 1)}
    for node1, node2 in cities:
        adj[node1].append(node2)
        adj[node2].append(node1)

    visited = set()
    total_cost = 0

    def dfs(node):
        nonlocal visited
        visited.add(node)
        return 1 + sum(dfs(neighbor) for neighbor in adj[node] if neighbor not in visited)

    for i in range(1, n + 1):
        if i not in visited:
            connected_nodes = dfs(i)
            total_cost += c_lib + (connected_nodes - 1) * c_road

    return total_cost


# MAIN
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
