# code -> https://leetcode.com/problems/single-number-iii/submissions/947954668/

''' 
Let's consider the example you provided earlier: nums = [0, 0, 1, 2].

We first calculate the XOR of all the numbers in the nums array:
xor = 0 ^ 0 ^ 1 ^ 2 = 3.

Next, we find the rightmost set bit in the xor value. In binary representation, 3 is 11, so the rightmost set bit is the bit at position 0 (from the right), which corresponds to the number 1. Therefore, rightmost_set_bit = 1.

Now, we iterate through each number in the nums array:

For the first number, num = 0:

num & rightmost_set_bit = 0 & 1 = 0.
Since the result is zero, we know this number belongs to the same group as xor2.
So, we update xor2 = xor2 ^ num = 0 ^ 0 = 0.
For the second number, num = 0:

num & rightmost_set_bit = 0 & 1 = 0.
Again, the result is zero, indicating that this number belongs to the same group as xor2.
xor2 = xor2 ^ num = 0 ^ 0 = 0.
For the third number, num = 1:

num & rightmost_set_bit = 1 & 1 = 1.
The result is non-zero, indicating that this number belongs to the same group as xor1.
xor1 = xor1 ^ num = 0 ^ 1 = 1.
For the fourth number, num = 2:

num & rightmost_set_bit = 2 & 1 = 0.
The result is zero, indicating that this number belongs to the same group as xor2.
xor2 = xor2 ^ num = 0 ^ 2 = 2.
Finally, we return [xor1, xor2], which gives us the two single numbers: [1, 2].

So, in this example, the code correctly identifies the two single numbers [1, 2] from the given input [0, 0, 1, 2].

'''

def singleNumber(self, nums: List[int]) -> List[int]:
        xor = nums[0]
        for i in range(1, len(nums)):
            xor = xor ^ nums[i]
        # xor = num1 ^ num2, need to separate both num1 and num2
        xor1, xor2 = 0, 0
        rightmost_set_bit = xor & (-xor)
        for i in range(len(nums)):
            if (nums[i] & rightmost_set_bit):
                xor1 = xor1 ^ nums[i]
            else:
                xor2 = xor2 ^ nums[i]

        return [xor1, xor2]
