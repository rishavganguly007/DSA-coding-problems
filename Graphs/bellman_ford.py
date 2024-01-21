# code : https://www.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/1
# resource : https://takeuforward.org/data-structure/bellman-ford-algorithm-g-41/

class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, edges, S):
        #code here
        # bellman-ford works on Directed Graph
        # it's alter to Djiksta's and provide soln for -ve wts and detects -ve cycle
        # iterate over the seqs n-1 times and check dist[u] + wt < dist[v] for {u, v, wt}
        
        max = 10**8
        dist = [max] * V
        dist[S] = 0
        
        for i in range(V):
            for u, v, wt in edges:
                if dist[u] != max and dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt
                    
        # to check for the -ve cycle will iterate for the Nth time and if any updates happen
        # then it's a -ve cycle
        for u, v, wt in edges:
                if dist[u] != max and dist[u] + wt < dist[v]:
                    return [-1] # as said in question
        
        return dist
