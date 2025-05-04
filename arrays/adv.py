"""
find subarray who has the largest sum. return sum
"""
def brute_force(nums):
    max_sum = float('-inf')
    for i in range(len(nums)):
        count = 0 
        for j in range(i, len(nums)):
            count += nums[j]
            max_sum = max(max_sum, count)
    return max_sum

"""
using kadanes, find subarray who has the largest sum. return sum
"""
def kadanes(nums):
    max_sum = nums[0]
    curr_sum = 0

    for num in nums:
        curr_sum = num + max(curr_sum, 0)
        max_sum = max(max_sum, curr_sum)

    return max_sum

"""
find the subarray in nums whose elements have the largest sum. return its first and last index
"""
def sliding_window(nums):
    max_sum = nums[0]
    curr_sum = 0
    maxL = maxR = L = 0
    

    for R in range(len(nums)):
        if curr_sum < 0:
            curr_sum = 0
            L = R
        
        curr_sum += nums[R]
        if curr_sum > max_sum:
            max_sum = curr_sum
            maxL, maxR = L, R
    
    return [maxL, maxR]
    






