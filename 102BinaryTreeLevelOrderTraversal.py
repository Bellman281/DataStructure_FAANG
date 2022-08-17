'''
102. Binary Tree Level Order Traversal
Given the root of a binary tree, return the level order traversal of its nodes' values. 
(i.e., from left to right, level by level).

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

'''

from typing import List
from pyparsing import Optional


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.right = right 
        self.left = left

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
