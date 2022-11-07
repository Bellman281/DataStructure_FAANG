'''
238. Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is
 equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
Input: nums = [1,2,3,4]
Output: [24,12,8,6]


'''
from typing import List


def productExceptSelf (nums: List[int]) -> List[int] :
        ans = [1] * len(nums)
        prefix = 1
        postfix = 1     
        for i in range(0,len(nums)):
            ans[i] = prefix
            prefix *= nums[i]
        print(ans)
        print(prefix)
        
        for i in range(len(nums)-1,-1,-1):
            print(ans)
            ans[i] = ans[i] * postfix
            postfix *= nums[i]
           
        return ans

print(productExceptSelf([1,200,3,223]))