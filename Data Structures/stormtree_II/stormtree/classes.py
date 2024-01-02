#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ***
# stormtree/classes.py
# CSCI211 Storm Tracker AVL Tree Exercise
# Last edited on 26/11/2023 by D. Mann
# ****
# Classes we're going to need, Storms and Node, plus a BST implementation.
# Libraries we need:
import logging,sys,argparse
log = logging.getLogger(__name__)


class Storm:
    # Actual class describing the storm data for stormtracker.
    name = ""
    year = 1900
    category = 1
    cost = 0

    def __init__(self,name,year,category,cost):
        self.name = name
        self.year = year
        self.category = category
        self.cost = cost

    def __str__(self):
        if self.category == 0:
            return f"Tropical Storm {self.name}, year: {self.year}, Cost: ${self.cost}B"
        else:
            return f"Hurricane {self.name}, year: {self.year}, Category: {self.category}; Cost: ${self.cost}B"

class StormNode:
    # Tree-type StormNode class, very basic implementation.
    # [L]eft:
    l = None
    # [R]ight:
    r = None
    # [S]torm:
    s = None
    # [H]eight/Level Counter:
    h = 1

    def set_storm(self,storm):
        self.s = storm

    def get_storm(self):
        return self.s

    def set_left(self, left):
        self.l = left

    def get_left(self):
        return self.l

    def set_right(self, right):
        self.r = right

    def get_right(self):
        return self.r



    def __str__(self):
        ostr = f"StormNode: Storm: {self.s},  Height: {self.h}, Cost: ${self.s.cost}B"
        return ostr

    # I'm Lazy... convenience:
    def __init__(self,name,year,category,cost):
        self.s = Storm(name,year,category,cost)



class AVLTree:
   root = False
   height = 0

   def _getHeight(self, node):
       if not node:
           return 0

       return node.h

   def _balance(self,node):
       if not node:
           return 0
       return self._getHeight(node.l) - self._getHeight(node.r)

   def _rotateLeft(self,node):
        right = node.r
        left2 = right.l
        # Rotate:
        right.l = node
        node.r = left2
        # Update Heights:
        node.h = 1 + max(self._getHeight(node.l), self._getHeight(node.r))
        right.h = 1 + max(self._getHeight(right.l), self._getHeight(right.r))

        # Return the new root:
        return right

   def _rotateRight(self, node):
       left = node.l
       right2 = left.r
       # Rotate:
       left.r = node
       node.l = right2
       # Update Heights:
       node.h = 1 + max(self._getHeight(node.l), self._getHeight(node.r))
       left.h = 1 + max(self._getHeight(left.l), self._getHeight(left.r))

       # Return the new root:
       return left




   def _inorder(self, node):
       """
       Perform an in-order Traversal
       :param node: Node
       """
       if not node: return
       self._inorder(node.l)
       #self.cout += f"Storm {node.s.name}, {node.s.year}, Damages: ${node.s.cost}B\n"
       self.cout += str(node.s)+"\n"
       self._inorder(node.r)

   def _postorder(self, node):
       """
       Perform a post-order Traversal
       :param node: Node
       """
       if not node: return
       self._inorder(node.l)
       self._inorder(node.r)
       #self.cout += f"Storm {node.s.name}, {node.s.year}, Damages: ${node.s.cost}B\n"
       self.cout += str(node.s) + "\n"

   def _preorder(self, node):
       """
       Perform a pre-order Traversal
       :param node: Node
       """
       if not node: return
       #self.cout += f"Storm {node.s.name}, {node.s.year}, Damages: ${node.s.cost}B\n"
       self.cout += str(node.s) + "\n"
       self._preorder(node.l)
       self._preorder(node.r)

   def traverse(self,node,type=0):
        """
        Perform a Traversal of the Tree
        :param type: Type of traversal to execute: 0: pre-order, 1: post-order, 2: in-order.
        :return: Traversal return String
        """
        self.cout = ""
        if type == 0:
            log.info("**Executing Pre-order Traversal***")
            self._preorder(node)
        elif type == 1:
            log.info("**Executing Post-order Traversal***")
            self._postorder(node)
        elif type == 2:
            log.info("**Executing in-order Traversal***")
            self._inorder(node)
        return(self.cout)

   def _printLevel(self, node, level):
       """
       PrintLevel function, critical for printing the tree in the right order
       while performing BFS
       :param node: Node to start algo from, usually self.root
       :param level:  Level for recursion control
       :return:
       """
       if not node:
           return
       if level == 1:
           print(node.s)
       elif level > 1:
           self._printLevel(node.l, level - 1)
           self._printLevel(node.r, level - 1)

   def bft(self,node):
       """
       Perform Breadth-first-traversal of the tree from the given node:
       """
       for i in range(1, node.h+1):
           print(f"***Level {i}***")
           self._printLevel(node, i)
           print(f"**************")
   def _insert(self, attr, node, new_node):
       if not node:
           return new_node
       # Normal BST Insertion first:
       if getattr(new_node.s, attr) > getattr(node.s, attr):
           # Going Right:
           node.r = self._insert(attr, node.r, new_node)
       elif getattr(new_node.s, attr) < getattr(node.s, attr):
           # Going Left:
           node.l = self._insert(attr, node.l, new_node)
       else:
           # NO duplicates allowed!
           raise Exception("Duplicate Value forbidden in BST.")

       # Now lets do Height updates of the ancestor node:
       node.h = 1 + max(self._getHeight(node.l), self._getHeight(node.r))

       # We're going to need the Balance factor:
       bal = self._balance(node)

       # If we're unbalanced; there are four possible ways to rebalance:

       # Case 1: Left,Left:
       log.info(f"Balance Currently: {bal}")
       if bal > 1 and getattr(new_node.s, attr) < getattr(node.l.s, attr):
           return self._rotateRight(node)
       # Case 2: Right, Right:
       if bal < -1 and getattr(new_node.s, attr) > getattr(node.r.s, attr):
           return self._rotateLeft(node)
       # Case 3:  Left, Right:
       if bal > 1 and getattr(new_node.s, attr) > getattr(node.r.s, attr):
           node.l = self._rotateLeft(node.l)
           return self._rotateRight(node)
       # Case 4: Right, Left:
       if bal < -1 and getattr(new_node.s, attr) < getattr(node.l.s, attr):
           node.r = self._rotateRight(node.r)
           return self._rotateLeft(node)

       # All done!!
       return node


   def insert(self,attr,node,new_node):
       if not self.root:
           log.info(f"AVL:_insert: AVL Tree Root Set to {new_node}")
           self.root = new_node
           self.height = 1
           return self.root, self.height
       else:
           log.info(f"AVL:_insert: {attr},{node},{new_node}")
           node = self._insert(attr,node,new_node)
           self.height = node.h
           return node,self.height
