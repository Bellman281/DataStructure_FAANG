### BST Class:
class Node():
  def __init__ (self, key):
    self.left = None
    self.right = None
    self.val = key
 

def insert(root,key):
    if root.val == key:
       return root
    elif root.val > key:
         root.left = insert(root.left,key)
    elif root.val < key :
         root.right = insert(root.right,key)
   

