# implementation of topo sort
# code -> https://leetcode.com/problems/course-schedule-ii/
# resource -> https://www.youtube.com/watch?v=WAOfKpxYHR8

from queue import Queue
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        '''
        tip: this ordering, if ans comes wrong try changing the arrows
        
            [[1,0],[2,0],[3,1],[3,2]]
            Graphically,
                         ______
                        |     ⬇️
               2 <- 0 <- 1 -> 3
               |______________⬆️
        '''
        for i in prerequisites:
            adj[i[1]].append(i[0])
        
        inDegree = [0] * numCourses

        for i in range(numCourses):
            for j in adj[i]:
                inDegree[j] += 1
        
        q = Queue()

        for i in range(numCourses):
            if inDegree[i] == 0:
                q.put(i)

        topo = []
        while not q.empty():
            node = q.get()
            topo.append(node)

            for i in adj[node]:
                inDegree[i] -= 1
            
                if inDegree[i] == 0:
                    q.put(i)
        
        return topo if len(topo) == numCourses else []
