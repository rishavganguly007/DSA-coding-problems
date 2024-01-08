# code : https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph-having-unit-distance/1
# resource : https://www.youtube.com/watch?v=C4gxoTaI71U

#User function Template for python3
from typing import List
from collections import defaultdict
from queue import Queue

class Solution:
    
    '''
    
    edge: [[0,1],[0,3],[3,4],[4 ,5],[5, 6],[1,2],[2,6],[6,7],[7,8],[6,8]] 
    
        0 - 1 - 2 -- 
        \           \
         3 - 4 - 5 - 6 - 7 - 8
                     \______/
                     
        need to find the dis, just like in bfs, we will keep a dist array instead of vis array
        so for eg,
        
        0 -1 dist is 1
    '''
    
    
    def shortestPath(self, edges, n, m, src):
        # code here
        adj = [[] for _ in range(n)]
        
        for u, v in edges:
            # u - v, u contains {v}, v contains {u}
            adj[u].append(v)
            adj[v].append(u)
        
        dist = [float('inf')] * n # create a distance array
        dist[src] = 0 # make src dist as 0
        q = Queue()
        q.put(src) # add src to queue
        
        while not q.empty():
            node = q.get()
            
            for i in adj[node]:
                if dist[node] + 1 < dist[i]:
                    dist[i] = dist[node] + 1
                    q.put(i)
                    
        ans = [-1] * n
        
        for i in range(n):
            if dist[i] != float('inf'):
                ans[i] = dist[i]
                
        return ans;

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = map(int, input().strip().split())
        edges=[]
        for i in range(m):
            li=list(map(int,input().split()))
            edges.append(li)
        src=int(input())
        ob = Solution()
        ans = ob.shortestPath(edges,n,m,src)
        for i in ans:
            print(i,end=" ")
        print()
        tc -= 1
# } Driver Code Ends
