# code -> https://leetcode.com/problems/container-with-most-water/description/
# Two - pointer approach
class Solution:
    def calculateStorage(self, i, j, height):
        length = min(height[i], height[j])
        breadth = abs(j - i)
        return length * breadth
    def maxArea(self, height: List[int]) -> int:
        max_store = 0
        left = 0
        right = len(height) - 1
        while left < right :
            max_store = max(max_store, self.calculateStorage(left, right, height))
            if height[left] < height[right]:
                left += 1
            else: 
                right -= 1 
        return max_store
