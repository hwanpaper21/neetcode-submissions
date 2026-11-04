# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        count = 0
        curr = head
        lst = set()

        while curr != None and curr not in lst:
            lst.add(curr)
            curr = curr.next
        if curr == None:
            return False
        else:
            return True
        