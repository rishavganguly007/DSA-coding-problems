def isCyclic(edges, v, e):

    # Write your code here.
    # Return bool type
    vis = [0] * v
    pathvis = [0] * v

    def dfs(node):
        vis[node] = 1
        pathvis[node] = 1

        # traverse for adjacent nodes
        for i in edges[node]:
            # when the node is not visited
            if vis[i] == 0:
                if dfs(i):
                    return True
            # when the node has previously visited 
            # but it has to be visited on the same path
            elif pathvis[i] == 1:
                return True

        pathvis[node] = 0
        return False


    for i in range(v):
        if vis[i] == 0:
            if dfs(i) :
                return True
    return False
