# code : https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1
# resource : https://www.youtube.com/watch?v=ZUFQfFaU-8U

from typing import List
from collections import defaultdict

class Solution:
    def topo_sort(self, node, adj, vis, st):
        vis[node] = 1
        for v, _ in adj[node]:
            if not vis[v]:
                self.topo_sort(v, adj, vis, st)
        st.append(node)
        
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        
        '''
        stp-1: do a topo-sort on the graph
        
        stp-2: tk node ot of stack (in dfs) and relax the edges, also track a dist array
        '''
        
        adj = defaultdict(list)
        
        for u, v, weight in edges:
            adj[u].append((v, weight))
            
        vis = [False] * n
        st = []
        
        for i in range(n):
            if not vis[i]:
                self.topo_sort(i, adj, vis, st)
                
        # do the distnace thing
        dist = [float('inf')] * n
        dist[0] = 0 # source node
        
        while st:
            node = st.pop()
            for v, wt in adj[node]:
                if dist[node] + wt < dist[v]:
                    dist[v] = dist[node] + wt
                    
        for i in range(n):
            if dist[i] == float('inf'):
                dist[i] = -1
        
        return dist
