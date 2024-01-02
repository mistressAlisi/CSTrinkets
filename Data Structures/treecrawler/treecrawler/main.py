#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ***
# stormtracker/main.py
# CSCI211 Storm Tracker Linked List Exercise
# Last edited on 09/24/2023 by D. Mann
# ****
# Main Driver Code
# Libraries we need:
import logging,csv

# Import the classes we need from our code:
from .classes import Storm,StormNode,StormLinkedList

log = logging.getLogger(__name__)
def main(file,col,prefix):
    log.info("Creating Linked Lists...")
    ll = StormLinkedList()
    log.info("parsing CSV file...")
    csvreader = csv.reader(file)
    # Read the header - it's contents will determine the structure of the TreeNodes:
    header = csvreader.__next__()

    loaded_data = []
    for storm_row in csvreader:
        # Create a Storm Linked list and Node instance for each row:
        log.info(f"Creating a new node for Storm {storm_row}")
        nst = StormNode(storm_row[0],storm_row[1],int(storm_row[2]),float(storm_row[3]))
        loaded_data.append(nst)
    # Now, append everything except the last note which we won't append  - we will insert at p. 14.
    last_node = loaded_data.pop()

    # Now, popuplate the linked list:
    for storm_row in loaded_data:
        ll.push(storm_row)
    # Finally, push the last_node into position 14:
    ll.insert(14,last_node)

    # Now, lets print out the output:
    # Don't iterate empty lists... please:
    if ll.get_count() == 0:
        log.error("Empty Linked list!!")
        return -1

    # Load the node and step through the list using the classic Linked list style:
    next = ll.get_head()
    while next != False:
        print(next.s)
        next = next.get_next()