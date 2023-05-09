# code -> https://leetcode.com/problems/rotate-list/submissions/947458129/
# resource -> https://www.youtube.com/watch?v=70tx7KcMROc&pp=ygUaa3VuYWwga2h1c2hhd2FzIGxpbmtlZCBsc3Q%3D

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k <= 0 or head == None or head.next == None:
            return head
        last: ListNode = head
        length: int  = 1
        while(last.next != None): # reach to the last node
            last = last.next
            length += 1

        last.next  = head # connect next of last with head
        rotations = k % length # get the amount of rotations needed
        skip = length - rotations 

        newLast: ListNode = head
        for i in range(skip - 1): # reach till the length - rotation node 
            newLast = newLast.next
        
        head = newLast.next # make it connect with head
        newLast.next = None # make new last node next to null
        return head

      
      
