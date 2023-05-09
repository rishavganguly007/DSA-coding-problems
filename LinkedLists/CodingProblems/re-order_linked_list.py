# code -> https://leetcode.com/problems/reorder-list/submissions/947441539/
# resource -> https://www.youtube.com/watch?v=70tx7KcMROc&pp=ygUaa3VuYWwga2h1c2hhd2FzIGxpbmtlZCBsc3Q%3D

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s: ListNode = head
        f: ListNode = head
        while f != None and f.next != None:
            s = s.next
            f = f.next.next
        return s

    def reverseLinkedList(self, head):
        # Write your code here.
        newHead = None
        while( head != None):
            next = head.next
            head.next = newHead
            newHead = head
            head = next
        return newHead

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None:
            return head
        mid: ListNode = self.middleNode(head)
        hf: ListNode = head
        hs: ListNode = self.reverseLinkedList(mid)

        #re-arrange
        while( hs != None and hf != None):
            temp = hf.next
            hf.next = hs
            hf = temp
            temp = hs.next
            hs.next = hf
            hs = temp

        # next of tail to null
        if (hf != None):
            hf.next = None
