# code -> https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1
# resource -> https://www.youtube.com/watch?v=BPlrALf1LDU&list=PLgUwDviBIf0rGEWe64KWas0Nryn7SCRWw&index=7

def detect(self, src, adj, vis):
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
