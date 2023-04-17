#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 18:21:41 2023

@author: marykyne
"""

# binary search tree algorithm
class TreeNode:
    
    def __Init__(self, value): # value we want to take as a node, three attributes
        self.left = None
        self.right = None
        self.value = value
        self.left = None
        self.right = None
        self.parent = None # points to parent node in a tree
        
    # define an insert fx
    def add(self, value):
        
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
        return self.delete_node(self.find(value))
    
    def delete_node(self,value):
        
        # finds smallest value on left
        def min_value_node(n):
            current=n
            while current.left!=None:
                current=current.left
            return current
        
        # return num of children attatched to the node
        def num_children(n):
            num_children=0
            
            if n.left!=None: 
                num_children +=1
            if n.right!=None: 
                num_children +=1
            
            return num_children
        
        # retrieves parent of deleted node
        self_parent=node.parent
        # retrieves children of deleted node
        node_children-num_children(node)
        
        # case one: no children
        
        if node_children == 0:
            if node_parent.left == node:
                node_parent.left=None
                
            else:
                node_parent.right=None
                
                
        # case two: node has 1 child
        
        if node_children==1:
            if node.left!=None:
                child=node.left
            else:
                child=node.right
            
            if node_parent.left==node:
                node_parent.left=child
            else:
                node_parent.right=child
            
            child.parent=node_parent
        
        # case three: node has two children
        
        if node_children==2:
            
            successor = min_value_node(node.right)
            node.value = successor.value
            
            self.delete_node(successor)
        
        
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

#print(tree.find(19)) # for find fx