# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        lst = []
        left = 0
        right = 0

        while curr != None:
            lst.append(curr)
            curr = curr.next
        right = len(lst) -1

        while left < right:
            head = lst[left]
            head.next = lst[right]
            head = head.next
            head.next = lst[left + 1]
  

            left += 1
            right -= 1
        lst[left].next = None

        