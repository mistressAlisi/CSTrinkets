#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ***
# stormtree/main.py
# CSCI211 Red/Black Storm Tracker AVL Tree Exercise
# Last edited on 26/11/2023 by D. Mann
# ****
# Main Driver Code
# Libraries we need:
import logging,csv

# Import the classes we need from our code:
from .classes import Storm,StormNode,AVLTree

log = logging.getLogger(__name__)
def main(file):
    # log.info("Creating Tree...")
    # ll = StormLinkedList()
    log.info("parsing CSV file...")
    csvreader = csv.reader(file)
    # skip header:
    csvreader.__next__()

    # Create a Red/Black BST
    tree = AVLTree()
    node = False
    height = 0
    for storm_row in csvreader:
        log.info(f"Creating a new node for Storm {storm_row}")
        nst = StormNode(storm_row[0],storm_row[1],int(storm_row[2]),float(storm_row[3]))
        node, height = tree.insert('cost',node,nst)
        log.info(f"Inserted  {nst.s.name} into tree. Height is: {height}")


    #Let's do some traversals:
    print("<---*****--->")
    log.info("Executing Traversals")
    print("Traversals Test...")
    print(tree.traverse(node,0))
    print("*****")
    print(tree.traverse(node,1))
    print("*****")
    print(tree.traverse(node,2))
    print("*****")
    log.info("Executing BFT")
    print("BFT/BFS Test...")
    tree.bft(node)
    print("<---*****--->")