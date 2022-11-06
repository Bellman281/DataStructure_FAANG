'''
350. Intersection of Two Arrays II

Given two integer arrays nums1 and nums2, 
return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays 
and you may return the result in any order.

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]


'''

from typing import List


def intersect(nums1: List[int], nums2:List[int]) -> int:
    result =[]
    dict1 = {k:(0,0) for k in nums1}

    for i in range(len(nums1)):
        if nums1[i] in dict1:
            dict1[nums1[i]] = (dict1[nums1[i]][0] + 1  , dict1[nums1[i]][1] )
    
    for i in range(len(nums2)):
        if nums2[i] in dict1:
            dict1[nums2[i]] = (dict1[nums2[i]][0], dict1[nums2[i]][1] + 1  )
    
    for k in dict1.keys():
        if dict1[k][1] > 0:
            rept = min(dict1[k][1],dict1[k][0])
            result.extend([k]*rept)
    return result


print(intersect([1,2,2,1],[2,2]))

print('Next case')

print(intersect([4,5,9],[9,4,9,8,4]))

print('Next case')

print(intersect([1,2,2,1,3,3],[2,3,3,4]))