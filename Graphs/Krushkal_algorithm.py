# resource : https://takeuforward.org/data-structure/kruskals-algorithm-minimum-spanning-tree-g-47/
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
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        
        edges = []
        
        for i in range(V):
            for adjNode, wt in adj[i]:
                edges.append((wt, (i, adjNode)))
        
        ds = DisjointSet(V)
        edges.sort(key=lambda x: x[0])
        mstWt = 0
        
        for wt, nodes in edges:
            u, v = nodes
            if ds.find_upar(u) != ds.find_upar(v):
                mstWt += wt
                ds.union_by_size(u, v)
        
        return mstWt
