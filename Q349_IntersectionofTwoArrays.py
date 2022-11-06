'''
349. Intersection of Two Arrays

Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must be unique and you may return the result in any order.

nums1 = [1,2,2,1], nums2 = [2,2]
'''
from typing import List


def intersection (nums1,nums2) -> List[int] :
        
        dict1 = {k:0 for k in nums1}
      
        for i in range(len(nums2)):
            if nums2[i] in dict1:
                dict1[nums2[i]] += 1

        return [k for k in dict1 if dict1[k]> 0 ]

print(intersection([1,2,2,1],[2,2,1]))

print(intersection([1],[1]))