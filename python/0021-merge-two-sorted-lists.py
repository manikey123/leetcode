# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


# Iterative
class ListNode:
    def __init__(self, x=0):
        self.val = x
        self.next = None

    def __str__(self):
        res=str(self.val)
        if self.next:
            res+=str(self.next)
        return res
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return dummy.next
    
# Recursive
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        lil, big = (list1, list2) if list1.val < list2.val else (list2, list1)
        lil.next = self.mergeTwoLists(lil.next, big)
        return lil
def convertListNode(x) -> ListNode:
    if x is None or len(x) ==0:
        return ListNode()
    l0 = ListNode(x[0])
    head = l0
    for i in x[1:]:
        l1=ListNode(i)
        l0.next =l1
        l0 = l1

    return head
list1 = convertListNode([1,2,4]); list2 = convertListNode([1,3,4])
output = Solution().mergeTwoLists(list1, list2)
print("output", output)