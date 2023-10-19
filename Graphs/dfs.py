# code -> https://practice.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1
# resource -> https://www.youtube.com/watch?v=Qzf1a--rhp8&list=PLgUwDviBIf0rGEWe64KWas0Nryn7SCRWw&index=5

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        vis = [False] * V
        vis[0] = True
        ls = []
        
        def dfs(node, vis, adj, ls):
        
            vis[node] = True
            ls.append(node)
            
            for i in adj[node]:
                if vis[i] == False:
                    dfs(i, vis, adj, ls)
                    
        dfs(0, vis, adj, ls)
        return ls
      
if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
