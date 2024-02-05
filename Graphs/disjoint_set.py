# resource: https://takeuforward.org/data-structure/disjoint-set-union-by-rank-union-by-size-path-compression-g-46/

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


# Main function
def main():
    # Create DisjointSet object with 7 elements
    ds = DisjointSet(7)

    # Perform union operations by size
    ds.union_by_size(1, 2)
    ds.union_by_size(2, 3)
    ds.union_by_size(4, 5)
    ds.union_by_size(6, 7)
    ds.union_by_size(5, 6)

    # Check if nodes 3 and 7 belong to the same set
    if ds.find_upar(3) == ds.find_upar(7):
        print("Same")
    else:
        print("Not same")

    # Perform another union operation and check again
    ds.union_by_size(3, 7)
    if ds.find_upar(3) == ds.find_upar(7):
        print("Same")
    else:
        print("Not same")


# Run the main function
if __name__ == "__main__":
    main()
