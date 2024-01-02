#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ***
# firestation/main.py
# CSCI211 Fire Station Linked List Exercise
# Last edited on 10/03/2023 by D. Mann
# ****
# Main Driver Code
# Libraries we need:
import logging,csv

# Import the classes we need from our code:
from .classes import FireStation,FireStationNode,StationLinkedList
from .sorters import _partition,linked_quick_sort,_linked_quick_sort
log = logging.getLogger(__name__)
def main(file):
    log.info("Creating Linked Lists...")
    ll = StationLinkedList()
    log.info("parsing CSV file...")
    csvreader = csv.reader(file)
    # skip header:
    csvreader.__next__()
    # Since we're taking the last item and not place it into the linked list at the end; we're going to do two passes,
    # The first pass will load the data into an array we can then manipulate. Then we will do the linked list loading.
    loaded_data = []
    for station_row in csvreader:
        # Create a Storm Linked list and Node instance for each row:
        log.info(f"Creating a new node for Station {station_row}")
        nst = FireStationNode(int(station_row[0]),station_row[1])
        ll.push(nst)
    # Now, append everything except the last note which we won't append  - we will insert at p. 14.

    # Now, lets print out the output:
    # Don't iterate empty lists... please:
    if ll.get_count() == 0:
        log.error("Empty Linked list!!")
        return -1
    print("\n****Printing List from head, forwards towards tail:***\n")
    next = ll.head
    print(next.station)
    while next != False:
        next = next.get_next()
        if (next != False):
            print(next.station)

    print("\n\n\n****EXECUTING QUICKSORT****\n\n\n")
    # OUR Quicksort algorithm executes in place!!!!
    linked_quick_sort(ll.head,ll.tail,'number')

    # Step forward from head to tail in the print:
    print("\n****Printing List from head, forwards towards tail:***\n")
    ll.printForward()

    # Step backwards from  tail to head in the print:
    print("\n****Printing List from tail, backwards towards head:***\n")
    ll.printBackward()