from typing import List

class Solution:
    def canPlaceFlowers1(self, flowerbed: List[int], n: int) -> bool:
        # Solution with O(1) space complexity
        empty = 0 if flowerbed[0] else 1

        for f in flowerbed:
            if f:
                n -= int((empty - 1) / 2)  # int division, round toward zero
                empty = 0
            else:
                empty += 1

        n -= (empty) // 2
        return n <= 0

    def canPlaceFlowers2(self, flowerbed: List[int], n: int) -> bool:
        # Another solution with O(1) space complexity
        for i in range(len(flowerbed)):
            if n == 0:
                return True
            # ensure the ends are covered with 0 check first and then the normal condition
            if ((i == 0 or flowerbed[i - 1] == 0) and
                    (flowerbed[i] == 0) and
                    (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)):
                flowerbed[i] = 1
                n -= 1

        return n == 0

    def canPlaceFlowers3(self, flowerbed: List[int], n: int) -> bool:
        # Solution with O(n) space complexity by embedding the ends with 0
        f = [0] + flowerbed + [0]

        for i in range(1, len(f) - 1):
            if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
                f[i] = 1
                n -= 1
        return n <= 0

    def canPlaceFlowers4(self, flowerbed: List[int], n: int) -> bool:
        # Initialize a counter to keep track of how many flowers have been planted
        count = 0

        # Iterate through each plot in the flowerbed
        for i in range(len(flowerbed)):
            # Check if the current plot is empty (0 represents an empty plot)
            if flowerbed[i] == 0:
                # Check if the current plot can have a flower planted in it. This is true if:
                # 1. It is the first plot, or the previous plot is empty (to its left)
                # 2. It is the last plot, or the next plot is empty (to its right)
                # This ensures no two flowers will be adjacent.
                if (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                    # Plant a flower in the current plot by marking it as '1'
                    flowerbed[i] = 1
                    # Increment the count of flowers planted
                    count += 1

                    # If the number of flowers planted is equal to or greater than the required number 'n',
                    # return True indicating success
                    if count >= n:
                        return True
        # After checking all plots, if the count of planted flowers is less than 'n',
        # return False indicating it's not possible to plant 'n' flowers without violating the rule
        return count >= n


# Create an instance of Solution
solution = Solution()

nums = [1, 0, 0, 0, 1]
target = 1
nums2 = [1, 0, 0, 0, 1]
target2 = 2
tuples = ((nums, target), (nums2, target2))

# Iterate through each solution method
for method in (solution.canPlaceFlowers1, solution.canPlaceFlowers2, solution.canPlaceFlowers3, solution.canPlaceFlowers4):
    for item in tuples:
        print(f"Using {method.__name__}: input: {item}, result: {method(item[0], item[1])}")
