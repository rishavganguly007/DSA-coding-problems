# code -> https://practice.geeksforgeeks.org/problems/bfs-traversal-of-graph/1
# resource -> https://www.youtube.com/watch?v=-tgVpUgsQ5k&list=PLgUwDviBIf0rGEWe64KWas0Nryn7SCRWw&index=4

from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        q = Queue()
        vis  = [False] * V
        bfs = []
        
        q.put(0)
        vis[0] = True
        
        while(not q.empty()):
            node = q.get()
            bfs.append(node)
            
            for i in adj[node]:
                if vis[i] == False:
                    vis[i] = True
                    q.put(i)
                    
        return bfs

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
