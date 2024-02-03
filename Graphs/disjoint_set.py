class DisjointSet:
    rank, parent = [], []

    def __init__(self, n):
        self.rank = [0] * n +1 # just to handle both 0 & 1 based indexing
        self.parent = [i for i in range(n+1)]
    
    def findUParent(self, node: int) -> int:     # to find ultimate parent
        if node == self.parent[node]:
            return node
        ultimate_parent = self.findUParent(self.parent[node])    
        self.parent[node] = ultimate_parent
        return self.parent[node]
    
    def unionByRank(self, u, v):
        ulp_u, ulp_v = self.findUParent(u), self.findUParent(v)
        if ulp_u == ulp_v: 
            return
        if self.rank[ulp_u] > self.rank[ulp_v]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1

if __name__ == "__main__":
    ds = DisjointSet(7)
    ds.unionByRank(1, 2)
    ds.unionByRank(2, 3)
    ds.unionByRank(4, 5)
    ds.unionByRank(6, 7)
    ds.unionByRank(5, 6)

    # Check if 3 and 7 are in the same set
    if ds.findUPar(3) == ds.findUPar(7):
        print("Same")
    else:
        print("Not Same")

    ds.unionByRank(3, 7)
    # Check again after union
    if ds.findUPar(3) == ds.findUPar(7):
        print("Same")
    else:
        print("Not Same")
