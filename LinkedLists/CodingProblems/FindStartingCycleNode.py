# code -> https://leetcode.com/problems/linked-list-cycle-ii/
# Resource -> https://youtu.be/70tx7KcMROc

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
  ''' 
  Algortihm to approach this problem:
  1. Find the length of the cycle
  
        a-b-c-d-e-f
            |     |
            g-h-i-j 
      so cycle starts at c, which is at pos = 3, length = 8
      
   2. take 2 pointers, f & s, traverse s-pointer till length and decrement the length, so it will reach at 'h'
      distance from h -> c is 2, also distance from a -> c is 2 and f is at 'a'
      
   3. Run f untill s, and increment both s and f, so eventualy both will travel 2 units to reach c which is the required node
  
  '''
    def findLength(self, head: Optional[ListNode]) -> int:
        # using slow-fast pointer approach
        fast: ListNode = head
        slow: ListNode = head

        while(fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                temp = slow.next
                length = 1
                # running an another while to run whithin the cycle and count the nodes
                while(temp != fast):
                    length += 1
                    temp = temp.next
                return length
        return 0

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = self.findLength(head) # 1. Got the length
        
        if length == 0:
            return None
          
        f: ListNode = head
        s: ListNode = head
        while(length > 0):  # 2. Run s till length 
            s = s.next
            length -= 1

        while(f != s):      # 3. run f till s to get the node
            f = f.next
            s = s.next
        return s
