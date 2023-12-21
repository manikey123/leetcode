# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # Use the iterative approach to remove duplicates
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next  # Skip the duplicate node
            else:
                current = current.next  # Move to the next node
        return head  # Return the modified list

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

# Example 1: head = [1,1,2]
list1 = create_linked_list([1, 1, 2])
assert linked_list_to_list(sol.deleteDuplicates(list1)) == [1, 2]

# Example 2: head = [1,1,2,3,3]
list2 = create_linked_list([1, 1, 2, 3, 3])
assert linked_list_to_list(sol.deleteDuplicates(list2)) == [1, 2, 3]

# Additional Test Cases
# Test with a list having no duplicates
list3 = create_linked_list([1, 2, 3])
assert linked_list_to_list(sol.deleteDuplicates(list3)) == [1, 2, 3]

# Test with an empty list
list4 = create_linked_list([])
assert linked_list_to_list(sol.deleteDuplicates(list4)) == []

print("All tests passed!")
