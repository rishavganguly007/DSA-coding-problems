# code: https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
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
