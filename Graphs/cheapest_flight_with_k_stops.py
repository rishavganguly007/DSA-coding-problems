# code : https://leetcode.com/problems/cheapest-flights-within-k-stops/
# resource : https://takeuforward.org/data-structure/g-38-cheapest-flights-within-k-stops/
from queue import Queue
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        # Create the adjacency list to depict airports and flights in
        # the form of a graph.
        adj = [[] for _ in range(n)]
        for it in flights:
            adj[it[0]].append((it[1], it[2]))

        # Create a queue which stores the node and their distances from the
        # source in the form of {stops, {node, dist}} with ‘stops’ indicating 
        # the no. of nodes between src and current node.
        q = deque([(0, (src, 0))])

        # Distance array to store the updated distances from the source.
        dist = [float('inf')] * n
        dist[src] = 0

        # Iterate through the graph using a queue like in Dijkstra with 
        # popping out the element with min stops first.
        while q:
            stops, (node, cost) = q.popleft()

            # We stop the process as soon as the limit for the stops reaches.
            if stops > K:
                continue

            for adjNode, edW in adj[node]:
                # We only update the queue if the new calculated dist is
                # less than the prev and the stops are also within limits.
                if cost + edW < dist[adjNode] and stops <= K:
                    dist[adjNode] = cost + edW
                    q.append((stops + 1, (adjNode, cost + edW)))

        # If the destination node is unreachable return ‘-1’
        # else return the calculated dist from src to dst.
        if dist[dst] == float('inf'):
            return -1
        return dist[dst]
        
