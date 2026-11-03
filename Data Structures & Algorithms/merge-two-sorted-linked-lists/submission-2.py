# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        templist = ListNode(-1)   
        curr1 = list1
        curr2 = list2
        tempcurr = templist

        while curr1 != None and curr2 != None:
            if curr1.val > curr2.val:
                tempcurr.next = curr2
                curr2 = curr2.next
            else:
                tempcurr.next = curr1
                curr1 = curr1.next

            tempcurr = tempcurr.next
        if curr1 == None:
            tempcurr.next = curr2
        else:
            tempcurr.next = curr1
        tempcurr = tempcurr.next
        return templist.next


