## https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/
## 26_ Easy Question
def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        if not(nums):
           return j
        for i in range(1,len(nums)):
          if nums[i]!=nums[j] :
             j += 1
             nums[j]=nums[i]
        return j+1
