#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ***
# stormtree/classes.py
# CSCI211 Storm Tracker Tree Exercise
# Last edited on 06/11/2023 by D. Mann
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
    l = False
    # [R]ight:
    r = False
    # [P]arent:
    p = False
    # [S]torm:
    s = False
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

    def set_parent(self, parent):
        self.p = parent

    def get_parent(self):
        return self.p


    # I'm Lazy... convenience:
    def __init__(self,name,year,category,cost):
        self.s = Storm(name,year,category,cost)
#

class BST:
    root = False
    cout = ""
    def _inorder(self,node=False):
        """
        Perform an in-order Traversal
        :param node: Node
        """
        if not node: return True
        self._inorder(node.l)
        self.cout += f"Storm {node.s.name}, {node.s.year}, Damages: ${node.s.cost}B\n"
        self._inorder(node.r)

    def _postorder(self,node=False):
        """
        Perform a post-order Traversal
        :param node: Node
        """
        if not node: return True
        self._inorder(node.l)
        self._inorder(node.r)
        self.cout += f"Storm {node.s.name}, {node.s.year}, Damages: ${node.s.cost}B\n"

    def _preorder(self,node=False,cout=""):
        """
        Perform a pre-order Traversal
        :param node: Node
        """
        if not node: return True
        self.cout += f"Storm {node.s.name}, {node.s.year}, Damages: ${node.s.cost}B\n"
        self._inorder(node.l)
        self._inorder(node.r)

    def _height(self,node):
        """
        Simple function to calculate tree height.
        :param node: The Node (send the root!)
        :return: Height in integers
        """
        if not node: return 0
        lh = self._height(node.l)
        rh = self._height(node.r)
        if lh > rh:
            return lh+1
        else:
            return rh+1

    def _printLevel(self,node, level):
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


    def _insert(self,attr,node,new_node,level=0):
        """
        Recursive function to insert into BST using attribute comparison.
        The function assumes an OBJECT for NODE with the attribute set in the 'attr' parameter present for all objects; inside the proper object:
        Ie. inside the storm object, node.s.attr must be set.
        Returns the level at which the insertion took place.
        THIS IS AN INTERNAL RECURSIVE FUNCTION, DO NOT CALL, CALL insert instead.
        :param attr: Attribute to compare with
        :param node: Root Node
        :param new_node: New Node
        :param level: Recursive Level (always pass as 0 for first call, default value is 0.)
        :return: level of insertion or FALSE if new node is empty.
        """
        # Don't do me dirty, bro:
        if not new_node: return False
        # Keep track of insertion level:
        level += 1
        if getattr(new_node.s,attr) > getattr(node.s,attr):
            # NEW NODE has a value greater than the current node, we'll try to descend right:
            if not node.r:
                # No Right node set, set it:
                node.r = new_node
                return level
            else:
                return self._insert(attr,node.r,new_node,level)
        elif getattr(new_node.s,attr) < getattr(node.s,attr):
            # NEW NODE has a value lesser than the current node, try to descend left:
            if not node.l:
                # No Right node set, set it:
                node.l = new_node
                return level
            else:
                return self._insert(attr,node.l,new_node,level)
        else:
            # NO duplicates allowed!
            raise Exception("Duplicate Value forbidden in BST.")

    def insert(self,attr,new_node):
        """
        Insert a new node to the tree, compare the values stored in 'attr'.
        :param attr: Attribute to compare values on.
        :param new_node: Node to be inserted
        :return: level of insertion
        """
        if not self.root:
            self.root = new_node
        else:
            return self._insert(attr,self.root,new_node,0)


    def traverse(self,type=0):
        """
        Perform a Traversal of the Tree
        :param type: Type of traversal to execute: 0: pre-order, 1: post-order, 2: in-order.
        :return: Traversal return String
        """
        self.cout = ""
        if type == 0:
            log.info("**Executing Pre-order Traversal***")
            self._preorder(self.root)
        elif type == 1:
            log.info("**Executing Post-order Traversal***")
            self._postorder(self.root)
        elif type == 2:
            log.info("**Executing in-order Traversal***")
            self._inorder(self.root)
        return(self.cout)

    def bft(self):
        """
        Perform Breadth-first-traversal of the tree.
        """
        h = self._height(self.root)
        for i in range(1, h + 1):
            print(f"***Level {i}***")
            self._printLevel(self.root, i)
            print(f"**************")