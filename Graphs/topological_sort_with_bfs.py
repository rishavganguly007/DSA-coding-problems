# code -> https://www.geeksforgeeks.org/problems/topological-sort/1
# resource -> https://www.youtube.com/watch?v=73sneFXuTEg
'''
------------------------------------------------------------------------------
Algo:

given Adj: 3: {0}, 1: {0}, 2: {0}

inDegree graph -> [3, 0, 0, 0] // tracks the incoming edges, 0 has 3 incoming edges
q -> 1,2 3
1st - node = 1
      q -> 2, 3
      topo = [1]
      inDegree = [2, 0, 0, 0]
2nd - node = 2
      q -> 3
      topo = [1, 2]
      inDegree = [1, 0, 0, 0]

3rd - node = 3
      q -> 
      topo = [1, 2, 3]
      inDegree = [0, 0, 0, 0]
      q -> 0
4th - node = 0
      q -> 
      topo = [1, 2, 3, 0]
      inDegree = [0, 0, 0, 0]

------------------------------------------------------------------------------
'''
from queue import Queue

class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        inDegree = [0] * V # list tracks number of incoming arrows
        
        for i in range(V):
            for j in adj[i]:
                inDegree[j] += 1
                
        q = Queue()
        
        for i in range(V):
            if inDegree[i] == 0:
                q.put(i)
                
        topo = []
        while not q.empty():
            node = q.get()
            topo.append(node)
            
            for i in adj[node]:
                inDegree[i] -= 1
                
                if inDegree[i] == 0:
                    q.put(i)
                    
        return topo



import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
    if N!=len(res):
        return False
    map=[0]*N
    for i in range(N):
        map[res[i]]=i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        
        for i in range(e):
            u,v=map(int,input().split())
            adj[u].append(v)
            
        ob = Solution()
        
        res = ob.topoSort(N, adj)
        
        if check(adj, N, res):
            print(1)
        else:
            print(0)
'''
Sample Input

1
3 4
3 0
1 0
2 0

'''
