'''
1608. Special Array With X Elements Greater Than or Equal X
You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.

Notice that x does not have to be an element in nums.

Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.

Input: nums = [0,4,3,0,4]
Output: 3
Explanation: There are 3 values that are greater than or equal to 3.

'''
from typing import List


class Solution:
    def specialArray(nums:List[int] =[0,4,3,0,4] ) -> int:        
        for i in range(1000):
            count = 0
            for t in nums:
                if t > i :
                    count +=1 
            return count

print(Solution.specialArray())