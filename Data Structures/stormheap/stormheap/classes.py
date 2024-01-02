#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ***
# main.py
# CSCI211: StormHeap: Storm Heap  Exercise
# Last edited on 05/12/2023 by D. Mann
# ****
import logging,csv
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

class MinHeap:
    def _heapify(self,array,attr,n,i):
        log.info(f"Heapify: Attr: {attr}, N:{n}, I: {i}")
        # Classic heapify: Set the max to the root:
        max = i
        # Now, take left and right:
        l = 2 * max + 1 # L is +1 of max.
        r = 2 * i + 2 # R is +2 of max.
        # Check for the existence of the left child to the root, and if it exists, if it's
        # Greater than root:
        if l < n:
            if getattr(array[max],attr) < getattr(array[l],attr):
                max = l
        # Now, same for the Right child:
        if r < n:
            if getattr(array[max],attr) < getattr(array[r],attr):
                max = r

        # Do a rootswap if needed:
        log.info(f"Heapify Max: {max}, I: {i}")
        if max != i:
            array[i], array[max] = array[max], array[i]
            # Then heapify root:
            log.info(f"Heapify descend, N {n},Max {max}, I {i}")
            self._heapify(array,attr,n,max)


    # Main heapsort driver code:
    def sort(self,array):
        alen = len(array)
        # Minheap it - start at the half of the array, alen/2 minus one:
        hs = alen // 2
        for r in range(hs -1, -1, -1):
            self._heapify(array,"cost",alen,r)

        # Now, step through the array and do an extraction/replacement in order:
        # And re-heapify after extraction.
        for r in range(alen-1,0,-1):
            array[r], array[0] = array[0], array[r]
            self._heapify(array,"cost",r,0)
