# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        ans = ListNode(0)
        temp = ans

        while l1 != None or l2 != None:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            total = x + y + carry
            carry = 0
            carry = total // 10
            temp.next = ListNode(total % 10)
            if l1: l1 = l1.next
            if l2: l2 = l2.next

            temp = temp.next

        if carry == 1:
            temp.next = ListNode(1)

        return ans.next