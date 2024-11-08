#code: https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    # res : https://leetcode.com/problems/maximum-xor-for-each-query/solutions/1163057/easy-o-n-solution-w-explanation-max-xor-2-maximumbit-1
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        maxXOR, arrayXOR, ans = (1 << maximumBit) - 1, reduce(ixor, nums), []
        for i in range(len(nums) - 1, -1, -1):
            ans.append(arrayXOR ^ maxXOR)
            arrayXOR ^= nums[i]
        return ans
