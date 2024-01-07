'''
There are N
 cities in the country. You want to travel from city 1
 to city N
. You wish to pick a flight path that lets you do so. However, there are a few conditions that need to be satisfied:

Not all cities have a flight connecting them. That is, you can go directly from city u
 to city v
 if and only if there is a flight that explicitly connects cities u
 and v
. Note that a flight that goes from city u
 to v
 also goes from v
 to u
. That is, it is a two-way flight.
Due to a new law in the country that monitors everyone's flight paths, there exist K
 triplets of cities of the form {ai,bi,ci}
 such that they cannot appear in the flight path in this exact order. Note that this means that for example they may appear as ai,ci,bi
.
For example, if N=5
, and {1,3,4}
 is a bad triplet, then, 1,2,1,3,4,5
 would be an illegal flight path, but, 1,2,3,1,4,5
 would be a legal one, assuming there are no other bad triplets and that all adjacent cities given in the path have a flight connecting them.

You want to minimize the number of flights you take so that the cost is minimal. So, find a way to start from city 1
 and end at city N
 while making sure the entire flight path follows the above conditions and taking as less flights as possible. If there are no such paths, output −1
. If there are multiple, output any of them.

Input
The first line of input contains three space-separated integers N,M,K
 (2≤N≤3000,1≤M≤20000,0≤K≤105
) representing the number of cities, flights and triplets respectively.

The next M
 lines describe the flights. The ith
 line consists of two integers u,v
 (1≤u,v≤N,u≠v
). Note that this implies the flight can travel from city u
 to v
 and the other-way around too.

The next K
 lines describe the triplets. The ith
 line consists of three integers ai,bi,ci
 (1≤ai,bi,ci≤N
). No triplet appears more than once in the list.

Output
If it is impossible to obtain a valid flight path, output −1
. Otherwise, output two lines. The first line containing a single integer x
 (2≤x≤N
) denoting the number of cities in the flight path. On the second line, output x
 integers describing the cities in the path denoting the shortest valid flight path from city 1
 to city N
. Note that both this trivially means that the path should start with 1
 and end with N
.

Examples
input
4 4 1
1 2
2 3
3 4
1 3
1 4 3
output
3
1 3 4 
input
3 1 0
1 2
output
-1
input
4 4 2
1 2
2 3
3 4
1 3
1 2 3
1 3 4
output
5
1 3 2 3 4 

'''
# problem - https://www.thejoboverflow.com/problem/400/

import sys
from collections import deque

def main():
    n, m, k = map(int, sys.stdin.readline().split())

    adj = [[] for _ in range(n + 1)]
    dist = [[float('inf')] * (n + 1) for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)

    forbidden = set()
    for _ in range(k):
        a, b, c = map(int, sys.stdin.readline().split())
        forbidden.add((a << 24) + (b << 12) + c)

    # BFS
    q = deque()
    q.append((0, 1))
    dist[0][1] = 0

    while q:
        v_first, v_second = q.popleft()

        for u in adj[v_second]:
            if ((v_first << 24) + (v_second << 12) + u) in forbidden:
                continue

            if dist[v_second][u] > dist[v_first][v_second] + 1:
                dist[v_second][u] = dist[v_first][v_second] + 1
                q.append((v_second, u))

    far = min(dist[i][n] for i in range(n))

    if far == float('inf'):
        print("-1")
        return

    path = deque([n])
    u = n
    for i in range(n):
        if path[0] == 1:
            break

        for j in range(n):
            if dist[j][u] == far:
                path.appendleft(j)
                u = j
                far -= 1
                break

    print(len(path))
    print(" ".join(map(str, path)))

if __name__ == "__main__":
    main()
