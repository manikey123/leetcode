class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """

    def minMeetingRooms(self, intervals):
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])

        res, count = 0, 0
        s, e = 0, 0
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res

intervals = [[0,30],[5,10],[15,20]]
intervals2 = [[7,10],[2,4]]
tuple = (intervals, intervals2)
# Input: [[0, 30], [5, 10], [15, 20]] Output: 2
# Input: [[7, 10], [2, 4]] Output: 1
s = Solution()
for item in tuple:
    print("Input:",item, "Output:", s.minMeetingRooms(item))