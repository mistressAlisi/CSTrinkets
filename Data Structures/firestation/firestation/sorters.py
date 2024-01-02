#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ***
# stormtracker/main.py
# CSCI211 Fire Station Linked List Exercise
# Last edited on 10/03/2023 by D. Mann
# ****
# Quicksort Sorting Library for Double Linked Lists
# Libraries we need:
import logging,csv
log = logging.getLogger(__name__)

# Classic Implementation of Quicksort using Pivot points:
# This implementation places the last element as the pivot,
# then evaluates the data contained to place the pivot in the correct position.
# Finally; it will put things smaller than the pivot to the left; and greater than the pivot to the right.

def _partition(start,stop,attr):
    # Take the pivot as last element:
    pivot = stop.get_data()
    # And take the previous element of the first element:
    i = start.get_prev()
    j = start
    # Partition forwards:
    while (j != stop):
        if (getattr(j.get_data(),attr) <= getattr(pivot,attr)):
            if (i == False):
                i = start
            else:
                i = i.next
            # here's a really clever trick, switch the DATA instead of the links in the list:
            t = i.get_data()
            i.set_data(j.get_data())
            j.set_data(t)
        j = j.next
    if (i == False):
        i = start
    else:
        i = i.get_next()
    t = i.get_data()
    i.set_data(stop.get_data())
    stop.set_data(t)
    return i

def _linked_quick_sort(start,stop,attr):
    if (start != None) and (start != stop) and (start != stop.next):
        temp_part = _partition(start,stop,attr)
        _linked_quick_sort(start,temp_part.prev,attr)
        _linked_quick_sort(temp_part.next,stop,attr)

def linked_quick_sort(first_node,last_node,attr):
    return _linked_quick_sort(first_node,last_node,attr)