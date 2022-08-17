'''
98. Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Input: root = [2,1,3]
Output: true

DFS 
In order : Left,Right,Right
Pre order : Root, Left, Right
Postorder : Left, Right, Root

'''

from pyparsing import Optional
import math

class TreeNode:
    def __init__ (self, val= 0, left =None, right= None):
        self.val   =   val 
        self.left  =  left
        self.right = right

class Solution: 
    def isValidBST(self, root: Optional(TreeNode)) -> bool:
        
        def validateNode ( node, low = -math.inf , high = math.inf):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False
            return (validateNode(node.right,node.val,high)  and validateNode(node.left,low,node.val))
            
        return validateNode(root)
        

