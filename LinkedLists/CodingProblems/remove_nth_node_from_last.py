# code -> https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/948632160/
# resource -> https://takeuforward.org/data-structure/remove-n-th-node-from-the-end-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        s: ListNode = head
        f: ListNode = head
        if head is None:
            return None

        for _ in range(n):
            f = f.next
        if f is None:
            return head.next

        while(f.next != None):
            f = f.next
            s = s.next
        s.next = s.next.next
        return head
