# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        left = temp
        right = temp.next
        count = 0
        
        while temp != None:
            count += 1
            temp = temp.next
        target = count - n -1
        for i in range(target):
            left = left.next
            right = right.next
        if target < 0:
            return head.next
        if right == None:
            return right
        right = right.next
        
        left.next = right
        return head
