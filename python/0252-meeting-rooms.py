class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """

    def canAttendMeetings(self, intervals):
        intervals.sort(key=lambda i: i[0])

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]

            if i1[1] > i2[0]:
                return False
        return True
intervals = [[0,30],[5,10],[15,20]]
intervals2 = [[7,10],[2,4]]
tuple = (intervals, intervals2)
# Input: [[0, 30], [5, 10], [15, 20]] Output: False
# Input: [[2, 4], [7, 10]] Output: True
s = Solution()
for item in tuple:
    print("Input:",item, "Output:", s.canAttendMeetings(item))