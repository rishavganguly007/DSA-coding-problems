# code: https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1
# resource : https://takeuforward.org/data-structure/minimum-spanning-tree-mst-using-prims-algo/

from queue import PriorityQueue

class Solution:
    
    def spanningTree(self, V, adj):
        """
        Finds the sum of weights of edges in the Minimum Spanning Tree (MST) using Prim's algorithm.

        Parameters:
        - V: Number of vertices in the graph.
        - adj: Adjacency list representing the graph. Each element is a list of tuples (neighbor, edge weight).

        Returns:
        - sumWt: Sum of weights of edges in the Minimum Spanning Tree.

        Prim's Algorithm Approach:
        1. Initialize an empty set 'vis' to keep track of visited nodes.
        2. Use a PriorityQueue 'pq' to store edges based on their weights. Initialize it with the first node (0) and no parent (-1).
        3. Initialize an empty list 'mst' to store the edges of the Minimum Spanning Tree.
        4. Initialize a variable 'sumWt' to store the sum of edge weights in the Minimum Spanning Tree.
        5. While the PriorityQueue is not empty:
            a. Get the edge with the minimum weight from the PriorityQueue.
            b. If the destination node is already visited, skip to the next iteration.
            c. Mark the destination node as visited.
            d. Add the current edge to 'mst'.
            e. Update 'sumWt' with the weight of the current edge.
            f. Explore neighbors of the current node:
                - If a neighbor is not visited, add it to the PriorityQueue.
        6. Return 'sumWt'.

        The 'mst' list contains the edges of the Minimum Spanning Tree, and 'sumWt' is the sum of their weights.
        """
        
        vis = set()  # Set to keep track of visited nodes.
        pq = PriorityQueue()  # Priority Queue to store edges based on their weights.
        pq.put((0, 0, -1))  # Initial edge weight, node, parent; starting with node 0 and no parent.
        mst = []  # List to store the edges of the Minimum Spanning Tree.
        sumWt = 0  # Variable to store the sum of edge weights in the Minimum Spanning Tree.
        
        while not pq.empty():
            edW, node, parent = pq.get()  # Get the edge with the minimum weight from the Priority Queue.
            
            if node in vis:
                continue  # Skip if the node is already visited (to avoid cycles).
            
            vis.add(node)  # Mark the node as visited.
            mst.append((parent, node))  # Add the current edge to the Minimum Spanning Tree.
            sumWt += edW  # Update the sum of edge weights.
            
            # Explore neighbors of the current node.
            for adjNode, wt in adj[node]:
                if adjNode not in vis:
                    pq.put((wt, adjNode, node))  # Add neighbors to the Priority Queue.
        print(mst)
        return sumWt  
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
