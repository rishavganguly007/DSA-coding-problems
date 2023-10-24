# code -> https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        def dfs(vis, node):
            vis[node] = 1

            for i in rooms[node]:
                if vis[i] == 0:
                    dfs(vis, i)
        
        vis = [0] * len(rooms)

        dfs(vis, 0 )

        for i in vis:
            if i == 0:
                return False
        
        return True
        
