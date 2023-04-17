#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 15:45:21 2023

@author: marykyne
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 18:21:41 2023

@author: marykyne
"""

# binary search tree algorithm
class TreeNode:
    
    def __init__(self, value): # value we want to take as a node, three attributes
        self.left = None
        self.right = None
        self.value = value
        self.left = None
        self.right = None
        self.parent = None # points to parent node in a tree
        
    # define an insert fx
    def insert(self, value):
        
        # if interted node's value is less than the current node, look left
        if value < self.value:
        
            if self.left is None:
                self.left = TreeNode(value) # if there isn't a node on left, it's this new value
                self.left.parent= self # set parent
                
            else:   # if there is a node there than insert fx
                self.left.insert(value)
                
        else:   # if the insert node is greater than value, right
        
            if self.right is None:
                self.right = TreeNode(value) # if there isn't a node on right, it's this new value
                self.right.parent = self # set parent
                
            else:   # if there is a node there than insert fx
                self.right.insert(value)

# traversing the tree using fxs; three methods
    
    def inorder_traversal(self):
        if self.left: # if left node exists, we're going to go to it
            
            self.left.inorder_traversal()
            
        print(self.value)
        
        if self.right: # if right node exists, we're going to go to it
            
            self.right.inorder_traversal()
            
    
    def preorder_traversal(self):
        
        print(self.value) # to print starting node

        if self.left: # if left node exists, we're going to go to it
            
            self.left.preorder_traversal()
                    
        if self.right: # if right node exists, we're going to go to it
            
            self.right.preorder_traversal()
            
            
    def postorder_traversal(self):
         
        if self.left: # if left node exists, we're going to go to it
             
            self.left.postorder_traversal()
                     
        if self.right: # if right node exists, we're going to go to it
             
            self.right.postorder_traversal()
             
        print(self.value) # at end because we cannot print something unless all leaf/child nodes have been printed (recursion)
   
    
    def find(self, value): # searching for node value
    
        if value < self.value:
            
            if self.left is None: # value cannot exist; value is less than current node and there's nothing to the left
                
                return False # value isn't part of the tree
            
            else:
                
                return self.left.find(value) # otherwise, return node's value
            
        elif value > self.value: # right/greater side
            
            if self.right is None: # value cannot exist; value is greater than current node and there's nothing to the left
                
                return False # value isn't part of the tree
            
            else:
                
                return self.right.find(value) # otherwise, return node's value
            
        else: # value is the same as the current node's
            
            return True
        
        
    def delete(self, value):
        if value < self.value: # find the value in the left tree
            if self.left is None: # if the data does not exist, return DNE
                print("The data does not exist in the tree.")
                return
            self.left = self.left.delete(value)
            return self # data is not deleted - yet
        
        elif value > self.value: # finding value in the right tree
            if self.right is None: # if the data does not exist, return DNE
                print("The data does not exist in the tree.")
                return 
            self.right = self.right.delete(value)
            return self # data is not deleted - yet
        
        else: 
            if self.left is None and self.right is None: # scans left and right children of the node
                return None # if there are no children, its a leaf (case 1) so we delete that 
            if self.left is None:
                return self.right # if there is only one child, we just delete the child
            if self.right is None:
                return self.left
            
            parent = self # setting temp values to be able to merge subtrees
            node = self.left 
            while node.right is not None: # finds the rightmost node to replace the node
                parent = node # no more need for parent to be parent, we change its use 
                node = node.right
            if parent.left is node: # last check for the left subtree to make sure everything is valid
                parent.left = None 
            else:
                parent.right = None
            self.value = node.value
            return self
        
        
tree = TreeNode(6)
tree.insert(5)
tree.insert(2)
tree.insert(4)
tree.insert(1)
tree.insert(2)
tree.insert(4)
tree.insert(19)
tree.insert(29)
tree.insert(11)
tree.insert(4)
tree.insert(2)


#tree.inorder_traversal() # the traversal in ascending order; smallest values to the furthest left possible

#tree.preorder_traversal() 

#tree.postorder_traversal() 

print(tree.find(19)) # for find fx




