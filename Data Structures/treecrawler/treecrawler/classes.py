#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ***
# stormtracker/classes.py
# CSCI211 Storm Tracker Linked List Exercise
# Last edited on 09/24/2023 by D. Mann
# ****
# Classes we're going to need, Storms and Nodes for Linked Lists.
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
    # Linked List StormNode class, very basic implementation.
    s = False
    n = False
    def set_storm(self,storm):
        self.s = storm

    def get_storm(self):
        return self.s

    def set_next(self, next):
        self.n = next

    def get_next(self):
        return self.n

    # I'm Lazy... convenience:
    def __init__(self,name,year,category,cost):
        self.s = Storm(name,year,category,cost)


class StormLinkedList:
    # Actual implementation of the linked list methods for the Stormtracker exercise

    head = False
    tail = False
    count = 0

    def get_count(self):
        return self.count

    def get_head(self):
        return self.head


    def insert(self,i,s):
        # Simple linked list logic, move to node i, then insert node s at that location in the linked list.
        if i > self.count:
            # If asking for something longer than the length of the whole list, just do a push:
            self.push(s)
        else:
            # Skip to node i and insert:
            c = 0
            next = self.head
            while c < i:
                next = next.get_next()
                c += 1
            # Now, get the next node that will become the next node -after- the inserted 's'
            curr_next = next.get_next()
            next.set_next(s)
            s.set_next(curr_next)
        log.info(f"At the bottom of LinkedList Insert; Count: {self.count}, insert @ {i} successful.")

    def push(self,s):
        # Simple Linked list logic, if count is 0, then head and tail must be False pointers.
        # If so, just set them both to the first (supplied) node:
        if self.count == 0:
            self.head = s
            self.tail = s
            self.count += 1
        else:
            # We're not at the start of the list, so instead of doing that, we'll link our node to the current tail node,
            # and then our current node becomes the new tail node.
            self.tail.set_next(s)
            self.tail = s
            self.count += 1
        log.info(f"At the bottom of LinkedList Push; Count: {self.count}")



class BST:
    root = False

    def insert(self,node,attr,value):
        if value > getattr(node,attr):
            # Value is grater than current node's value, insert down the right branch:
            if (node.