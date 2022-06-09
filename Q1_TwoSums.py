### Question1
[https://leetcode.com/problems/two-sum/]
###
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map={}
        for i in range(len(nums)):
            hash_map [nums[i]] = i
        
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hash_map and hash_map[comp] != i :
                return [i,hash_map[comp]]
