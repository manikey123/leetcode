# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists_iterative(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Iterative Approach
        dummy = ListNode()  # Create a dummy node to simplify edge cases
        tail = dummy        # Tail node of the new list

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # If one of the lists is not empty, append it to the end
        tail.next = list1 if list1 else list2

        return dummy.next  # Return the merged list, excluding the dummy node

    def mergeTwoLists_recursive(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Recursive Approach
        if not list1 or not list2:
            return list1 or list2

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists_recursive(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists_recursive(list2.next, list1)
            return list2

# Test cases
sol = Solution()

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


# Example 1
list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])
merged_list = sol.mergeTwoLists_iterative(list1, list2)
assert linked_list_to_list(merged_list) == [1, 1, 2, 3, 4, 4]

# Example 2
list1 = create_linked_list([])
list2 = create_linked_list([])
merged_list = sol.mergeTwoLists_iterative(list1, list2)
assert linked_list_to_list(merged_list) == []

# Example 3
list1 = create_linked_list([])
list2 = create_linked_list([0])
merged_list = sol.mergeTwoLists_iterative(list1, list2)
assert linked_list_to_list(merged_list) == [0]

# Additional Test Cases
list1 = create_linked_list([2, 4, 6])
list2 = create_linked_list([1, 3, 5])
merged_list = sol.mergeTwoLists_iterative(list1, list2)
assert linked_list_to_list(merged_list) == [1, 2, 3, 4, 5, 6]

list1 = create_linked_list([5])
list2 = create_linked_list([1, 3, 7])
merged_list = sol.mergeTwoLists_iterative(list1, list2)
assert linked_list_to_list(merged_list) == [1, 3, 5, 7]

print("All tests passed!")