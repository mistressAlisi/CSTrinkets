#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ***
# main.py
# CSCI211: StormHeap: Storm Heap  Exercise
# Last edited on 05/12/2023 by D. Mann
# ****
# Main Driver Code
# Libraries we need:
import logging,csv

# Import the classes we need from our code:
from .classes import Storm,MinHeap

log = logging.getLogger(__name__)



def printStorms(storm_array):
    i = 0
    for storm in storm_array:
        print(f"Storm Array: Item {i}: Storm: {storm.name} - Cost: ${storm.cost}B")
        i += 1

def main(file):
    # log.info("Creating Tree...")
    # ll = StormLinkedList()
    log.info("parsing CSV file...")
    csvreader = csv.reader(file)
    # skip header:
    csvreader.__next__()

    # Work array:
    work_array = []
    node = False
    height = 0
    for storm_row in csvreader:
        log.info(f"Creating a new node for Storm {storm_row}")
        node = Storm(storm_row[0],storm_row[1],int(storm_row[2]),float(storm_row[3]))
        work_array.append(node)
    print("<---*****--->")
    print("Initial Array - pre-heapsort:")
    printStorms(work_array)
    print("<---*****--->")
    hs = MinHeap()
    hs.sort(work_array)
    print("MinHeap sort....")
    printStorms(work_array)
    print("<---*****--->")