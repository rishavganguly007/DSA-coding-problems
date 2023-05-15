# code -> https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        store = 0
        carry = 0
        node = ListNode()
        l3: ListNode = ListNode()
        node = l3
        temp1 = l1
        temp2 = l2
        while (temp1 != None or temp2 != None or carry == 1):
            val = 0
            if temp1 != None:
                val += temp1.val
                temp1 = temp1.next
            if temp2 != None:
                val += temp2.val
                temp2 = temp2.next
            val += carry
            carry = int( val / 10)
            newNode = ListNode(val = val % 10)
            node.next = newNode
            node = node.next

        return l3.next
