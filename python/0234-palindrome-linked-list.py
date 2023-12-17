class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def isPalindrome_reverseSecondHalf(self, head: ListNode) -> bool:
        if not head or not head.next:  # Check for empty or single-node list
            return True

        # Find the middle of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the list
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # Compare the first half and the reversed second half
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left, right = left.next, right.next
        return True

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

# Example 1: head = [1,2,2,1]
list1 = create_linked_list([1, 2, 2, 1])
assert sol.isPalindrome_reverseSecondHalf(list1) == True

# Example 2: head = [1,2]
list2 = create_linked_list([1, 2])
assert sol.isPalindrome_reverseSecondHalf(list2) == False

# Additional Test Cases
# Single-element list
list3 = create_linked_list([1])
assert sol.isPalindrome_reverseSecondHalf(list3) == True

# Empty list
list4 = create_linked_list([])
assert sol.isPalindrome_reverseSecondHalf(list4) == True

# Non-palindrome list of even length
list5 = create_linked_list([1, 2, 3, 4])
assert sol.isPalindrome_reverseSecondHalf(list5) == False

print("All tests passed!")
