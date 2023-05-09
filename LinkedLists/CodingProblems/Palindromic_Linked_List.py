# resource -> https://www.youtube.com/watch?v=70tx7KcMROc&pp=ygUaa3VuYWwga2h1c2hhd2FzIGxpbmtlZCBsc3Q%3D
# code -> https://leetcode.com/problems/palindrome-linked-list/submissions/947419307/


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

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid: ListNode = self.middleNode(head)
        headSecond: ListNode = self.reverseLinkedList(mid)
        reverseHead: ListNode = headSecond

        while(head != None and headSecond != None):
            if head.val != headSecond.val:
                break
            head = head.next
            headSecond = headSecond.next

        self.reverseLinkedList(reverseHead)
        return head == None or headSecond == None
