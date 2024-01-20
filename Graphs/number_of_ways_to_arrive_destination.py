# code: https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/description/
# resource : https://takeuforward.org/data-structure/g-40-number-of-ways-to-arrive-at-destination/

from queue import PriorityQueue
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        # create adjacent matrix
        for i in roads:
            adj[i[0]].append((i[1], i[2]))
            adj[i[1]].append((i[0], i[2]))

        pq  = PriorityQueue()
        pq.put((0, 0))
        dist = [float('inf')] * n
        dist[0] = 0
        ways = [0] * n
        ways[0] = 1

        mod = 10**9 + 7

        while not pq.empty():
            dis, node = pq.get()

            for adjNode, edN in adj[node]:
                # coming fist time with short distance
                if dis + edN < dist[adjNode]:
                    dist[adjNode] = dis + edN
                    pq.put((dis + edN, adjNode))
                    ways[adjNode] = ways[node]
                elif dis + edN == dist[adjNode]:
                    ways[adjNode] = (ways[node] + ways[adjNode]) % mod
        return ways[n-1] % mod


        
        
