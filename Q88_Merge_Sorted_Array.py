## Q88. Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/
#####



class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1[0:m]
        #defeine tow pointers to read and one to write
        pr1, pr2, pw = 0, 0 , 0
        while (pw < m + n):
            if (pr2>= n or (pr1<m and nums1_copy[pr1] <= nums2[pr2] ) ):
                nums1[pw] = nums1_copy[pr1]
                pr1 += 1
            else:
                nums1 [pw] = nums2[pr2]
                pr2 += 1
            pw +=1
        return nums1
