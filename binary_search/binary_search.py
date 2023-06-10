import math
def binary_search(arr, target: int) -> bool:
  low: int = 0
  high: int = len(arr) - 1

  while(high >= low):
    mid = math.floor((low + high) / 2)
    
    if arr[mid] == target:
      return True
    if target > arr[mid]:
      low = mid +1
    elif target < arr[mid]:
      high = mid - 1
  return False

print(binary_search([1,2,3,4,5,7,9], 7))
