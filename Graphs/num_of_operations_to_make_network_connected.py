# code: https://leetcode.com/problems/number-of-operations-to-make-network-connected/
# resource : strver vdo

class DisjointSet:
    def __init__(self, n):
        # Initialize rank, parent, and size arrays
        self.rank = [0] * (n + 1)
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find_upar(self, node):
        # Find the representative (parent) of the set to which the node belongs
        if node == self.parent[node]:
            return node
        # Path compression: Update the parent to the representative during traversal
        self.parent[node] = self.find_upar(self.parent[node])
        return self.parent[node]

    def union_by_rank(self, u, v):
        ulp_u = self.find_upar(u)
        ulp_v = self.find_upar(v)

        # Union by rank: Attach the shorter rank tree to the taller rank tree
        if ulp_u == ulp_v:
            return
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1

    def union_by_size(self, u, v):
        ulp_u = self.find_upar(u)
        ulp_v = self.find_upar(v)

        # Union by size: Attach the smaller size tree to the larger size tree
        if ulp_u == ulp_v:
            return
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        ds = DisjointSet(n)
        extraEdge = 0
        for u, v in connections:
            if ds.find_upar(u) == ds.find_upar(v):
                extraEdge += 1
            ds.union_by_size(u, v)
        
        numOfComponents = 0
        for i in range(n):
            if i == ds.parent[i]:
                numOfComponents += 1
        
        return numOfComponents-1 if extraEdge >= (numOfComponents - 1) else -1
        
sl = Solution()
print(sl.makeConnected(6, [[0,1],[0,2],[0,3],[1,2]]))

        
