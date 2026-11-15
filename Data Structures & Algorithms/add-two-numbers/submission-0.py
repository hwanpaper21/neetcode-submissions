# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        templ1 = ""
        templ2 = ""
        sum = 0
        ans = ListNode(0)
        temp = ans
        while l1 != None:
            templ1 = str(l1.val) + templ1
            l1 = l1.next
        while l2 != None:
            templ2 = str(l2.val) + templ2
            l2 = l2.next        
        sum = int(templ1) + int(templ2)

        for i in range(len(str(sum))):
            temp.next = ListNode(str(sum)[len(str(sum))-i-1])
            temp = temp.next
        
        return ans.next

