# code -> https://leetcode.com/problems/find-eventual-safe-states/description/
# resource -> https://www.youtube.com/watch?v=uRbJ1OF9aYM

from queue import Queue
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        '''
        terminal nodes - outgoing nodes / outdegree = 0
         as topo-sort is all about inDegrees, therefore reverse the path/edges
         - reverse edges
         - flow plain topo-sort ie get all nodes with indegre = 0 and remove all
           the adjacent nodes

        '''
        v = len(graph)
        adjRev = [[] for _ in range(v)]
        inDegree = [0] *v

        for i in range(v):
            # from i -> it to i <- it

            for j in graph[i]:
                adjRev[j].append(i)
                inDegree[i] += 1

        q = Queue()

        safeNodes = []

        for i in range(v):
            if inDegree[i] == 0:
                q.put(i)

        while not q.empty():
            node = q.get()
            safeNodes.append(node)

            for i in adjRev[node]:
                inDegree[i] -= 1
                if inDegree[i] == 0:
                    q.put(i)

 
        safeNodes.sort()
        return safeNodes

        
