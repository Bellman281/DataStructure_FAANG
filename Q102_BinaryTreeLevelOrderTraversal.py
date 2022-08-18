'''
102. Binary Tree Level Order Traversal
Given the root of a binary tree, return the level order traversal of its nodes' values. 
(i.e., from left to right, level by level).

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Solution: 
Breadth First Search (BFS)
We scan through the tree level by level, following the order of height, from top to bottom.
The nodes on higher level would be visited before the ones with lower levels.


'''

from typing import List
import collections
from pyparsing import Optional


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.right = right 
        self.left = left

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        
        
        #initiate the queue with a root and start from level 0
        q = collections.deque()
        q.append( root )
        
        # while queue is not empty
        while q :
            
            # start the current level by an empty list
            level = []
            # compute the number of elements in current level
            qLen = len(q)
            
            #loop through the elements.
            for i in range(qLen):
                # popout all the elements from the queue 
                node = q.popleft()
                
                if node:
                   ## add each element to the current level and their child into queue for next level
                   level.append(node.val)
                   q.append(node.left)
                   q.append(node.right)
            if level:
                result.append(level)
        return result
                

        
        
        
