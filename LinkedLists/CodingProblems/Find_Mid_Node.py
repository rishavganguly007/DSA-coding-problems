# code -> https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  ''' 
  Use the approach of slow-fast pointer
  '''
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s: ListNode = head
        f: ListNode = head
        while f != None and f.next != None:
            s = s.next
            f = f.next.next
        return s
