from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Using Hash Map
        def using_hash_map() -> bool:
            num_dict = {}  # Initialize an empty dictionary
            for i, num in enumerate(nums):  # Iterate through the array with index
                if num in num_dict and i - num_dict[num] <= k:  # Check if num is in dict and within k distance
                    return True  # Return True if duplicate within k distance is found
                num_dict[num] = i  # Update the dictionary with the current number and its index
            return False  # Return False if no duplicate within k distance is found

        # Using Set (Sliding Window)
        def using_set() -> bool:
            num_set = set()  # Initialize an empty set
            for i, num in enumerate(nums):  # Iterate through the array with index
                if num in num_set:  # Check if num is already in the set
                    return True  # Return True if duplicate is found
                num_set.add(num)  # Add the current number to the set
                if len(num_set) > k:  # Check if the size of the set exceeds k
                    num_set.remove(nums[i - k])  # Remove the oldest element in the set
            return False  # Return False if no duplicate is found

        # You can switch between the two methods here
        return using_hash_map()
        # return using_set()

# Test Cases
sol = Solution()
assert sol.containsNearbyDuplicate([1,2,3,1], 3) == True  # Example 1
assert sol.containsNearbyDuplicate([1,0,1,1], 1) == True  # Example 2
assert sol.containsNearbyDuplicate([1,2,3,1,2,3], 2) == False  # Example 3

# Additional Test Cases
assert sol.containsNearbyDuplicate([1,2,3,4,5,6,7,8,9,1], 10) == True
assert sol.containsNearbyDuplicate([1,2,3,4,5,6,7,8,9,10], 5) == False
