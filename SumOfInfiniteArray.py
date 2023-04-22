#Code -> https://www.codingninjas.com/codestudio/problems/sum-of-infinite-array_873335
def calculatePos(arr, n, pos):
    if pos == -1:
        return 0
    repeat = int(pos / n)
    extra = pos % n
    if extra >= 0 and pos!= -1:
        val = arr[n-1]*repeat + arr[extra]
    else:
        val = arr[n-1]*repeat
        
    return val
def sumInRanges(arr, n, queries, q):

    # Write your function Here.
    dp = []
    sum = 0
    q_list = []

    # This is called prefix-sum, didn't know, but anyway have a lil pat on back for ya, good job!!!
    for i in range(n):
        sum += arr[i]
        dp.append(sum)
    # Till this
    for i in range(q):
        L = queries[0] - 1
        R = queries[1] - 1
        l1 = calculatePos(dp, n, L-1)
        r1 = calculatePos(dp,n, R)
        val = r1 - l1
        q_list.append(val % (10 ** 9 + 7))
    return q_list
# Naive appraoch            
def naaiveApproach(arr, n, queries, q):
  q_list = []
  for i in range(q):
    L = queries[i][0]
    R = queries[i][1]
    sum = 0
    for j in range(L, R+1):
      sum = sum + arr[j % n - 1]
      q_list.append(sum)
    return q_list           

queries = [0] *2 
queries[0], queries[1] = 1, 2          

print(sumInRanges([10], 1, queries, 1))     
