# code -> https://www.codingninjas.com/codestudio/problems/799897
# code -> https://leetcode.com/problems/reverse-linked-list/submissions/947294863/
# resource -> https://www.youtube.com/watch?v=70tx7KcMROc&pp=ygUaa3VuYWwga2h1c2hhd2FzIGxpbmtlZCBsc3Q%3D


''' 
given: head-1->2->3->4
to make: 1<-2<-3<-4-head

take 3 pointers - prev ( points to previous node ) 
                  present ( points to present node ) & 
                  next  ( points to next node )
1. make the present.next to prev
2. increment prev to present
3. next to next.next
'''
from math import *
from collections import *
from sys import *
from os import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        prev: ListNode = None
        present: ListNode = head
        Next: ListNode = present.next
        while(present != None):
            present.next = prev
            prev = present
            present = Next
            if Next != None:
                Next = Next.next

        head = prev
        return head

