# code -> https://leetcode.com/problems/is-graph-bipartite/
# resource -> https://www.youtube.com/watch?v=-vu34sct1g8

from queue import Queue
class Solution:
    def bfs(self, start, graph, color):
        q = Queue()
        q.put(start)
        color[start] = 0
        while not q.empty():
            node = q.get()

            for i in graph[node]:
                if color[i] == -1:
                    color[i] = 1 - color[node] 
                    q.put(i)
                elif color[i] == color[node]:
                    return False
        return True
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1] * len(graph)
        def bfs(start):
            q = Queue()
            q.put(start)
            color[start] = 0
            while not q.empty():
                node = q.get()

                for i in graph[node]:
                    if color[i] == -1:
                        color[i] = 1 - color[node] 
                        q.put(i)
                    elif color[i] == color[node]:
                        return False
            return True

        for i in range(len(graph)):
            if color[i] == -1:
                if bfs(i) == False:
                    return False
        return True

        
        
        
