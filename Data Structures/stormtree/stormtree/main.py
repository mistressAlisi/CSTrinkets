#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ***
# stormtracker/main.py
# CSCI211 Storm Tracker Tree Exercise
# Last edited on 06/11/2023 by D. Mann
# ****
# Main Driver Code
# Libraries we need:
import logging,csv

# Import the classes we need from our code:
from .classes import Storm,StormNode,BST

log = logging.getLogger(__name__)
def main(file):
    # log.info("Creating Tree...")
    # ll = StormLinkedList()
    log.info("parsing CSV file...")
    csvreader = csv.reader(file)
    # skip header:
    csvreader.__next__()

    # Create a BST
    tree = BST()
    for storm_row in csvreader:
        log.info(f"Creating a new node for Storm {storm_row}")
        nst = StormNode(storm_row[0],storm_row[1],int(storm_row[2]),float(storm_row[3]))
        level = tree.insert('cost',nst)
        log.info(f"Inserted node for storm at level {level}")

    # Let's do some traversals:
    print(tree.traverse(0))
    print("*****")
    print(tree.traverse(1))
    print("*****")
    print(tree.traverse(2))
    print("*****")
    log.info("Executing BFT")
    tree.bft()
    print("*****")