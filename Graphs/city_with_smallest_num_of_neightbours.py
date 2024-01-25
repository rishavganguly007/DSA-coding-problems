# code: https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/
# resource : https://takeuforward.org/data-structure/find-the-city-with-the-smallest-number-of-neighbours-at-a-threshold-distance-g-43/
class Solution:
    def findTheCity_BellmanFord(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]

        for i in edges:
            dist[i[0]][i[1]] = i[2]
            dist[i[1]][i[0]] = i[2]
        for i in range(n):
            dist[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] == float('inf') or dist[k][j] == float('inf'):
                        continue
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        cityCount = n
        cityNum = -1
        for city in range(n):
            cnt = 0
            for adjCity in range(n):
                if dist[city][adjCity] <= distanceThreshold:
                    cnt += 1
            if cnt <= cityCount:
                cityCount = cnt
                cityNum = city
        return cityNum

    def findTheCity_Djikstras(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = [[] for _ in range(n)]
        # add paths in adj list
        for node1, node2, wt in edges:
            adj[node1].append((node2, wt))
            adj[node2].append((node1, wt))

        # djikstras
        def djikstras(s):
            dist = [float('inf')] * n
            dist[s] = 0
            pq = PriorityQueue()
            pq.put((0, s))

            while not pq.empty():
                dis, node = pq.get()

                for adjNode, edW in adj[node]:
                    if dis + edW < dist[adjNode]:
                        dist[adjNode] = dis + edW
                        pq.put((dis + edW, adjNode))
            return dist             

        min_count = float('inf')
        res = -1
        for i in range(n):
            count = sum(1 for d in djikstras(i) if d <= distanceThreshold ) - 1
            '''
            for i = 0,
            djikstras(0) will return dist list as [0,2,5,5,4] as per eg 2 (edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]] )

            among dist, 0, 2 will be under threshold, so 2 will taken in sum 
            count(1 + 1), then count will be sum - 1 (not consider 0 as it is src)
            '''
            if count < min_count:
                min_count = count
                res = i
            elif count == min_count:
                res = max(res, i)

        return res

