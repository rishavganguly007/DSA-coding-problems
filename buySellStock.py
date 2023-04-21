#code -> https://www.codingninjas.com/codestudio/problems/893405

from os import *
from sys import *
from collections import *
from math import *

def maximumProfit(prices):
    # Write your code here.
    profit = 0
    mini = prices[0]
    for i in range(1, len(prices)):
        cost = prices[i] - mini
        profit = max(cost, profit)
        mini = min(mini, prices[i])

    return profit
p =   maximumProfit([17,20,11,9,12,6])
print(p)
