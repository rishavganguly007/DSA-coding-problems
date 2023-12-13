# The code is exactly equal to topological sort code, if the size is == V then there is no cycle, else there is

from queue import Queue
class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        inDegree = [0] * V # list tracks number of incoming arrows
        
        for i in range(V):
            for j in adj[i]:
                inDegree[j] += 1
                
        q = Queue()
        
        for i in range(V):
            if inDegree[i] == 0:
                q.put(i)
                
        c = 0
        while not q.empty():
            node = q.get()
            c += 1
            
            for i in adj[node]:
                inDegree[i] -= 1
                
                if inDegree[i] == 0:
                    q.put(i)
                    
        return not c == V 

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
