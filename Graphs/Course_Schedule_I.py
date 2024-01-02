# implementation of topo sort
# code -> https://leetcode.com/problems/course-schedule/
# resource -> https://www.youtube.com/watch?v=WAOfKpxYHR8

from queue import Queue
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # creating adj matrix, 
        # [[],[],[],[],]
        # [0, 1] => [[1],[],[],[],]
        adj = [[] for _ in range(numCourses)]
        for i in prerequisites:
            adj[i[0]].append(i[1])

      # Rest is Topo Sort  
      inDegree = [0] * numCourses

        for i in range(numCourses):
            for j in adj[i]:
                inDegree[j] += 1
        q = Queue()

        for i in range(numCourses):
            if inDegree[i] == 0:
                q.put(i)
        
        c = 0

        while not q.empty():
            node = q.get()
            c += 1

            for i in adj[node]:
                inDegree[i] -= 1
                
                if inDegree[i] == 0:
                    q.put(i)
                    
        return c == numCourses 
        
        
