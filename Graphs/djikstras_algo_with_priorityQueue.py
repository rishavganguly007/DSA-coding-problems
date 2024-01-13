# code -> https://www.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1
# resource -> https://www.youtube.com/watch?v=V6H1qAeB-l4

'''
1. Initialization:
   - Create a priority queue to store vertices based on their current shortest distance from the source.
   - Initialize a distance array 'dist' with all distances set to infinity, except the source vertex set to 0.
   - Start by placing the source vertex in the priority queue with its distance as 0.

2. Algorithm Process:
   - While the priority queue is not empty:
     a. Dequeue the vertex with the minimum distance from the priority queue.
     b. For each adjacent vertex of the dequeued vertex:
        - Calculate a new tentative distance.
        - If this new distance is shorter than the current known distance, update it.
        - Enqueue the adjacent vertex with its new shortest distance into the priority queue.

3. Priority Queue:
   - Simulate the priority queue using a list sorted based on distances. 
   - The vertex with the smallest distance will always be at the front, enabling efficient vertex selection.

4. Result:
   - After processing all vertices, the 'dist' array will contain the shortest distances from the source vertex to all other vertices.
   - This array serves as the output, showcasing the shortest path lengths from the source to each vertex in the graph.
'''

from queue import PriorityQueue
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        pq = PriorityQueue()
        
        dist = [float('inf')] * V # creating a distance array
        
        dist[S] = 0
        pq.put((0,S))
        
        while not pq.empty():
            dis, node = pq.get()
            
            for it in adj[node]:
                adjNode, weight  = it
                
                if dis + weight < dist[adjNode]:
                    dist[adjNode] = dis + weight
                    pq.put((dist[adjNode], adjNode))
                    
        return dist


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } 
