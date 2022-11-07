'''
26. Remove Duplicates from Sorted Array
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

Do not allocate extra space for another array. 
You must do this by modifying the input array in-place with O(1) extra memory.


'''
from typing import List
def removeDuplicates(nums: List [int]) -> int:
    k = 1
    seen = nums[0]
    for i in range(1, len(nums)):
        
        if nums[i] != seen:
           nums[k] = nums[i]
           k += 1
           seen = nums[i]
        
    return k

print(removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4] ))