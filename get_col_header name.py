"""
 a value of n for which there is a coresponding alphabet that lies between A-Z

so suppose n = 1 then output is "A" 
n = 5, Output is "E"
n = 26 Output is "Z"
n = 27 Output is "AA"
n = 52 Output is "AZ"

and so on ...
"""

def getColoumnTitle(n):
  dict = {0:"Z",1:"A", 2: "B", 3: "C", 4: "D", 5: "E", 6:"F",7:"G",8:"H",9:"I",10:"J",11:"K",12:"L",13:"M",14:"N",15:"O",
          16:"P",17:"Q",18:"R",19:"S",20:"T",21:"U",22:"V",23:"W",24:"X",25:"Y"}
  temp = n
  s = ""

  while temp > 0:
    q = temp % 26
    
    if temp == 0:
      q = q-1
    s += dict[q]
    
    temp = int(temp/26)
    print(temp)

  return s[::-1]


n =  int(input())
print(getColoumnTitle(n))
