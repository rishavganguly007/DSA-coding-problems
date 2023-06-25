# code -> https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/
# resource -> https://youtu.be/MG-Ac4TAvTY

class Solution:
    def reqDays(self,weights, cap):
        n = len(weights)
        days = 1
        load = 0
        for i in range(n):
            if load + weights[i] > cap:
                days += 1
                load = weights[i]
            else:
                load += weights[i]
        return days



    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        low = max(weights)
        high = sum(weights)
        while low <= high:
            mid = (low + high) // 2
            d = self.reqDays(weights, mid)
            if  d <= days:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
            
                
        return ans
