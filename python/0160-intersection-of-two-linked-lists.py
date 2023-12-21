from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode_twoPointer(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1, l2 = headA, headB
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1

    def getIntersectionNode_hashTable(self, headA: ListNode, headB: ListNode) -> ListNode:
        # Hash Table Approach
        nodes_in_A = set()
        current = headA
        # Traverse list A and store each node's reference in a set
        while current:
            nodes_in_A.add(current)
            current = current.next

        current = headB
        # Traverse list B and check if any node is in the set
        while current:
            if current in nodes_in_A:
                return current  # Intersection found
            current = current.next

        return None  # No intersection
# Helper function to create a linked list from a list
def create_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Function to create intersecting linked lists
def create_intersecting_lists(lstA, lstB, intersectVal):
    if not lstA or not lstB:
        return None, None

    # Create two separate lists
    headA = create_linked_list(lstA)
    headB = create_linked_list(lstB)

    # If no intersection
    if intersectVal is None:
        return headA, headB

    # Find intersecting node in listA
    currentA = headA
    while currentA and currentA.val != intersectVal:
        currentA = currentA.next

    # Attach the intersecting node to the end of listB
    currentB = headB
    while currentB.next:
        currentB = currentB.next
    currentB.next = currentA

    return headA, headB

# Test cases with assert statements
sol = Solution()

# Example 1
listA1, listB1 = create_intersecting_lists([4, 1, 8, 4, 5], [5, 6, 1], 8)
assert sol.getIntersectionNode_twoPointer(listA1, listB1).val == 8

# Example 2
listA2, listB2 = create_intersecting_lists([1, 9, 1, 2, 4], [3], 2)
assert sol.getIntersectionNode_twoPointer(listA2, listB2).val == 2

# Example 3
listA3, listB3 = create_intersecting_lists([2, 6, 4], [1, 5], None)
assert sol.getIntersectionNode_twoPointer(listA3, listB3) is None

# Additional Test Case with no intersection
listA4, listB4 = create_intersecting_lists([1, 2, 3], [4, 5, 6], None)
assert sol.getIntersectionNode_twoPointer(listA4, listB4) is None

print("All tests passed!")
