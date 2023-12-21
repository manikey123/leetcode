class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # Value of the node
        self.next = next  # Pointer to the next node

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # Fast and Slow Pointer Approach
        slow = fast = head  # Initialize both pointers to the head of the list
        while fast and fast.next:  # Continue until fast reaches the end of the list
            slow = slow.next  # Move slow pointer one step
            fast = fast.next.next  # Move fast pointer two steps
        return slow  # When fast reaches the end, slow is at the middle

# Helper function to create a linked list from a list
def create_linked_list(lst):
    if not lst:
        return None  # Return None for an empty list
    head = ListNode(lst[0])  # Create the head node
    current = head  # Initialize current node
    for value in lst[1:]:  # Iterate over the list values
        current.next = ListNode(value)  # Create and link new node
        current = current.next  # Move to the new node
    return head  # Return the head of the linked list

# Helper function to convert linked list to list
def linked_list_to_list(node):
    result = []  # Initialize an empty list
    while node:  # Traverse the linked list
        result.append(node.val)  # Append node value to the list
        node = node.next  # Move to the next node
    return result  # Return the list representation of the linked list

# Test cases with assert statements
sol = Solution()

# Example 1
list1 = create_linked_list([1, 2, 3, 4, 5])
assert linked_list_to_list(sol.middleNode(list1)) == [3, 4, 5]  # Check if the middle node is as expected

# Example 2
list2 = create_linked_list([1, 2, 3, 4, 5, 6])
assert linked_list_to_list(sol.middleNode(list2)) == [4, 5, 6]  # Check if the middle node is as expected

# Additional Test Cases
list3 = create_linked_list([1])
assert linked_list_to_list(sol.middleNode(list3)) == [1]  # Test with a single-element list

list4 = create_linked_list([])
assert linked_list_to_list(sol.middleNode(list4)) == []  # Test with an empty list

print("All tests passed!")

# Time and Space Complexity
# Time Complexity: O(n), where n is the number of nodes in the list.
# Space Complexity: O(1), as no additional space is used.
