# code -> https://leetcode.com/problems/number-of-provinces/
# resource -> https://www.youtube.com/watch?v=ACzkVtewUYA&pp=ygUWc3RyaXZlciBjb3VudCBwcm92aW5jZQ%3D%3D

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def dfs(node, vis):
            vis[node] =  1
            for i in adj[node]:
                if vis[i] == 0:
                    dfs(i, vis)


        row = len(isConnected)
        col = len(isConnected[0])

        adj = [[] for _ in range(row)]

        for i in range(row):
            for j in range(col):
                if isConnected[i][j] == 1 and i != j:
                    adj[i].append(j)

        vis = [0] * len(adj)
        count = 0

        for i in range(len(adj)):
            if vis[i] != 1:
                count += 1
                dfs(i, vis)    

        return count    
