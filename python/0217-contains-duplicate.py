from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset: # return true when in hashset
                return True
            hashset.add(n)  #keep adding into array by default
        return False
list1 = [1,2,3,1]
list2 = [1,2,3,4]
list3 = [1,1,1,3,3,4,3,2,4,2]
list4 = [0,1]
list = [ list1,list2, list3, list4 ]

# Result:
# [1, 2, 3, 1] : True
# [1, 2, 3, 4] : True
# [1, 1, 1, 3, 3, 4, 3, 2, 4, 2] : True
# [0, 1] : True

s = Solution()
for item in list:
    print(item, ":", s.containsDuplicate(list1))
