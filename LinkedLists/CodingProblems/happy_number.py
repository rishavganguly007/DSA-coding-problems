
''' 
n = 10
10 = 1^2 + 0^2 = 1 , hence Happy Number

use the concept of cycle detection in linked-list
'''
def isHappy(n: int) -> bool:
        s: int = getHappy(n)
        f: int = getHappy(getHappy(n))
        if f == 1 or s == 1:
              return True
        while s != f:
          if f == 1 or s == 1:
              return True
          s = getHappy(s)
          f = getHappy(getHappy(f))
          if s == f:
            return False
            
    
def getHappy(n: int) -> int:
  val = 0
  while(n > 0):
    modulo = n % 10
    val += modulo * modulo
    n = int(n/10)
  return val

print(isHappy(10))
