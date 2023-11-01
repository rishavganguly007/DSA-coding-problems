# code -> https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        vis = [0] * len(graph)
        pathvis = [0] * len(graph)
        chk = [0] * len(graph)

        def dfs(node):
            vis[node] = 1
            pathvis[node] = 1
            chk[node] = 0

            for i in graph[node]:
                if vis[i] == 0:
                    if dfs(i) == True:
                        return True
                elif pathvis[i] == 1:
                    return True
            chk[node] = 1
            pathvis[node] = 0
            return False
        safenode = []
        for i in range(len(graph)):
            if vis[i] == 0:
                dfs(i) 
        for i in range(len(graph)):
            if chk[i] == 1:
                safenode.append(i)

        return safenode


