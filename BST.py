### BST Class:
class Node():
  def __init__ (self,left = None, right = None ,key):
    self.left = left
    self.right = right
    self.val = key
 

def insert(root,key):
    if root is None:
       return Node(key) 
    if root.val == key:
       return root
    elif root.val > key:
         root.left = insert(root.left,key)
    elif root.val < key :
         root.right = insert(root.right,key)
   

