# Definition for singly-linked list.


class ListNode:
    def __init__(self, x=0):
        self.val = x
        self.next = None
    # def __str__(self):
    #
    #     return str(self.val) + "" + self.next
    def __str__(self):
        res=str(self.val)
        if self.next:
            res+=str(self.next)
        return res
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

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


s = [1,2,3,4,5]
s2 = [1,2]
s3 = []

t1 = convertListNode(s)
t2 = convertListNode(s2)
t3 = convertListNode(s3)

tuple = ( t1, t2, t3)
for item in tuple:
    print("Input:",item)
    output = Solution().reverseList(item)
    print("output", output)
