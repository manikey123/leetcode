# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements_iterative(self, head: ListNode, val: int) -> ListNode:
        # Iterative Approach
        while head and head.val == val:
            head = head.next  # Skip the nodes from the beginning that need to be removed

        current = head
        while current and current.next:
            if current.next.val == val:
                current.next = current.next.next  # Skip the node
            else:
                current = current.next  # Move to the next node
        return head  # Return the modified list

    def removeElements_dummy(self, head: ListNode, val: int) -> ListNode:
        # dummy Node Approach
        dummy = ListNode(0, head)  # Create a dummy node
        prev, current = dummy, head
        while current:
            if current.val == val:
                prev.next = current.next  # Remove the node
            else:
                prev = current  # Move prev to current
            current = current.next  # Move to the next node
        return dummy.next  # Return the modified list, excluding the dummy node

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

# Helper function to convert linked list to list
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Test cases with assert statements
sol = Solution()

# Example 1: head = [1,2,6,3,4,5,6], val = 6
list1 = create_linked_list([1, 2, 6, 3, 4, 5, 6])
assert linked_list_to_list(sol.removeElements_iterative(list1, 6)) == [1, 2, 3, 4, 5]
assert linked_list_to_list(sol.removeElements_dummy(list1, 6)) == [1, 2, 3, 4, 5]

# Example 2: head = [], val = 1
list2 = create_linked_list([])
assert linked_list_to_list(sol.removeElements_iterative(list2, 1)) == []
assert linked_list_to_list(sol.removeElements_dummy(list2, 1)) == []

# Example 3: head = [7,7,7,7], val = 7
list3 = create_linked_list([7, 7, 7, 7])
assert linked_list_to_list(sol.removeElements_iterative(list3, 7)) == []
assert linked_list_to_list(sol.removeElements_dummy(list3, 7)) == []

# Additional Test Cases
# Test with a list having no elements to remove
list4 = create_linked_list([1, 2, 3])
assert linked_list_to_list(sol.removeElements_iterative(list4, 4)) == [1, 2, 3]
assert linked_list_to_list(sol.removeElements_dummy(list4, 4)) == [1, 2, 3]

print("All tests passed!")
