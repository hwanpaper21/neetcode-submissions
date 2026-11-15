# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        left = temp
        count = 0
        
        while temp != None:
            count += 1
            temp = temp.next
        target = count - n -1

        if count == n:
            return head.next

        for i in range(target):
            left = left.next
        left.next = left.next.next
        
        return head
