''''
257. Binary Tree Paths:
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

'''

from typing import List
from pyparsing import Optional


class TreeNode(object):
    "Definition of a binary tree node"
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self,root: Optional[TreeNode]) -> List(str):
        result = []
        if not root:
            return result
        def construct_paths(root,path):
            if root:
                path += str(root.val)
            if not root.left and not root.right:
                result.append(path)
            else:
                path += "->" 
                construct_paths(root.left,path)
                construct_paths(root.right,path)
        construct_paths(root,"")
        return result
