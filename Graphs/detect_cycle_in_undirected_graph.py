# code -> https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1
# resource -> https://www.youtube.com/watch?v=BPlrALf1LDU&list=PLgUwDviBIf0rGEWe64KWas0Nryn7SCRWw&index=7

def detect_By_BFS(self, src, adj, vis):
        vis[src] = True
        q = Queue()
        q.put([src, -1])

        while not q.empty():
            ele = q.get()
            node = ele[0]
            parent = ele[1]

            for i in adj[node]:
                if not vis[node]:
                    vis[node] = True
                    q.put([i, node])
                else:
                    if parent != i:
                        return True
        return False

def detect_By_DFS(self, src, adj, vis, parent):
        vis[src] = True
        for i in adj[src]:
            if not vis[i]:
                if self.detect_By_DFS(i, adj, vis, src):
                    return True
            elif i != parent:
                return True
        return False

def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
        vis = [False] * V
        for i in range(V):
            if not vis[i]:
                if self.detect_By_DFS(i, adj, vis, -1) :
                    return True
        return False
  
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")
