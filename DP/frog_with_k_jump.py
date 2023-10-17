# code -> https://www.codingninjas.com/studio/problems/minimal-cost_8180930?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0
# resource -> https://www.youtube.com/watch?v=Kmh3rhyEtB8&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=5

from typing import *

def f(ind, k, heights, dp):
    # if n <= 0:
    #     return 0
    # mini = 10**10

    # for i in range(1, k+1):
    #     if n-i >= 0:
    #         val = f(n-i,i, heights ) + abs(heights[n]-heights[n-i] )
    #         mini = min(val, mini)
    # return val
    if ind == 0:
        return 0
    # If the result for this index has been previously calculated, return it.
    if dp[ind] != -1:
        return dp[ind]

    mmSteps =10**10

    # Loop to try all possible jumps from '1' to 'k'
    for j in range(1, k + 1):
        # Ensure that we do not jump beyond the beginning of the array
        if ind - j >= 0:
            # Calculate the cost for this jump and update mmSteps with the minimum cost
            jump = f(ind - j, k,  heights, dp) + abs(heights[ind] - heights[ind - j])
            mmSteps = min(jump, mmSteps)

    # Store the minimum cost for this index in the dp array and return it.
    dp[ind] = mmSteps
    return dp[ind]

def minimizeCost(n : int, k : int, heights : List[int]) -> int:
    # Write your code here.
    dp = [-1] * n 
    return f(n-1, k, heights, dp)
