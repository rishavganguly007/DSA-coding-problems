'''
There is a simple greedy algorithm for this problem.

At first, there are n elements in ascending order, in order for them to be distinct, each element should be greater than its predecessor by at least one.

so, we have

1, 2, 3 ... , n

Now, the sum of all n number is n*(n + 1)/2

What is left is left = N - n*(n + 1)/2

In order to keep the last element as small as possible, we need to scatter the left difference to all numbers

so, we have

1 + left/n, 2 + left/n, ..., n + left/n

If left % n != 0, we just need to add extra 1 to the last left % n elements.

Note: if N < n*(n + 1)/2, there is no solution

'''


def getNumOfDistinctPartitons(N: int, k: int) -> [] :
    sumOfK = int((k *(k+1))/2)
    partition = []
    if N < sumOfK:
        return []
    
    remaining = N - sumOfK
    
    divide = int(remaining / k)
    remainder = remaining % k
    
    for i in range(k):
        if i == k - 1:
            partition.append(i + 1 + divide + remainder)
            break
        partition.append(i + 1 + divide)
    return partition
            
    

print (getNumOfDistinctPartitons(80, 10))
