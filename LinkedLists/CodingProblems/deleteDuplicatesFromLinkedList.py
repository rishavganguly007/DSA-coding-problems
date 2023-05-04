#Code -> https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node: ListNode = head
        if head == None:
            return 
        while(node.next != None):
            if node.val == node.next.val: # checks if the next elements hold the same val or not
                node.next = node.next.next # if true, assigns the addres of the next to next addres to the current node
            else:
                node = node.next
        return head
