# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList_iterative(self, head: ListNode) -> ListNode:
        # Iterative Approach
        prev, curr = None, head
        while curr:
            next_temp = curr.next  # Store the next node
            curr.next = prev       # Reverse the link
            prev = curr            # Move prev to current node
            curr = next_temp       # Move to the next node
        return prev  # Prev will be the new head after the list is reversed

    def reverseList_recursive(self, head: ListNode) -> ListNode:
        # Recursive Approach
        if not head or not head.next:
            return head
        p = self.reverseList_recursive(head.next)
        head.next.next = head
        head.next = None
        return p

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

# Test cases
sol = Solution()

# Test case 1
head = create_linked_list([1, 2, 3, 4, 5])
print(linked_list_to_list(sol.reverseList_iterative(head)))  # Output: [5, 4, 3, 2, 1]

# Test case 2
head = create_linked_list([1, 2])
print(linked_list_to_list(sol.reverseList_iterative(head)))  # Output: [2, 1]

# Test case 3
head = create_linked_list([])
print(linked_list_to_list(sol.reverseList_iterative(head)))  # Output: []

# Additional test cases
head = create_linked_list([1])
print(linked_list_to_list(sol.reverseList_recursive(head)))  # Output: [1]
