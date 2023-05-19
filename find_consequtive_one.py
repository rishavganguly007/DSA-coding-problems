# code -> https://leetcode.com/problems/max-consecutive-ones/description/
# used 2 pointer approach
def consec1(arr):
  p1, p2 = 0, 0
  store = 0

  for i in range(len(arr)):
    if arr[i] == 0:
      store = max( store, p2 - p1)
      p2+= 1
      p1 = p2
    elif arr[i] == 1:
      p2 += 1
  store = max(store, p2 - p1)
  return store

print(consec1([0,0,1,0]))
