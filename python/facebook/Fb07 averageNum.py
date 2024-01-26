# From: http://codingbat.com/prob/p126968
# Return the "centered" average of an array of ints, which we'll
# say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the
# smallest value, ignore just one copy, and likewise for the largest
# value. Use int division to produce the final average. You may assume that the array is length 3 or more.


def centered_average(nums):
     b=nums
     ma=max(b)
     mi=min(b)
     l=(len(b)-2)

     s=sum(b)-max-min
     avg=int(s/l)

     return avg

def centered_average(nums):
    sorted_list= sorted(nums)
    return sum(sorted_list [1:-1]/(len(sorted_list)-2))

def center_average_2(nums):
    #sorted(nums)
    nums.sort()
    nums2= nums[1:-1]
    return sum(nums2)// len(nums2)



assert center_average_2([1, 2, 3, 4, 100]) == 3
assert center_average_2([1, 1, 5, 5, 10, 8, 7]) == 5
assert center_average_2([-10, -4, -2, -4, -2, 0]) == -3
