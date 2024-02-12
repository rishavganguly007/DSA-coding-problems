# code : https://www.hackerrank.com/challenges/bfsshortreach/

#!/bin/python3

import math
import os
import random
import re
import sys
from queue import Queue

def bfs(n, m, edges, s):
    # Write your code here
    adj = [[] for _ in range(n+1)]
    
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        
    q = Queue()
    dist = [float('inf')] * (n+1)
    
    dist[s] = 0
    q.put(s)
    
    while not q.empty():
        u = q.get()
        
        for node in adj[u]:
            if dist[u] + 6 < dist[node]:
                dist[node] = dist[u] + 6
                q.put(node)
    
    res = []
    for i in range(1, n+1):
        if i != s:
            if dist[i] == float('inf'):
                dist[i] = -1
            res.append(dist[i])
        
    return res



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
