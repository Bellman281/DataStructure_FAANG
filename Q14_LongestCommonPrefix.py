'''
14.Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


Input: strs = ["flower","flow","flight"]
Output: "fl"


'''
from typing import List


class Solution:
    def longestCommonPrefix (self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = ""
        s = zip(*strs)
        for i in s:
            if len(set(i)) == 1 :
                prefix += i[0]
            else:
                break
        return prefix

S = Solution()
print(S.longestCommonPrefix(["flower","flow","flight"]))
