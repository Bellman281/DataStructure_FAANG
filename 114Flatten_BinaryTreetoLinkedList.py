'''
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the 
        right child pointer points to the next node in the list and the left child pointer is always null.

The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

'''
class TreeNode:
    def __init__(self, left = None, right = None, val = 0):
        self.val = val
        self.right = right 
        self.left = left

class Solution:
    def flatten(self, root: TreeNode)-> None:
        '''
        Do not return anything just modify root in-place instead.
        '''    
        def tree_flatten (root):
            if not root:
                return None
            # flatten sub trees
            leftTail  = tree_flatten(root.left)
            rightTail = tree_flatten(root.right)

            if root.left:
                leftTail.right = root.right
                root.right = root.left
                root.left = None
            
            last = rightTail or leftTail or root

            return last
        
        tree_flatten(root)
            