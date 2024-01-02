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

    def getCategory(self):
        return self.category

    def getCost(self):
        return self.cost

    def getName(self):
        if self.category == 0:
            return f"Tropical Storm {self.name}"
        else:
            return f"Hurricane {self.name} (cat: {self.category})"

    def __str__(self):
        if self.category == 0:
            return f"Tropical Storm {self.name}, year: {self.year}, Cost: ${self.cost}B"
        else:
            return f"Hurricane {self.name}, year: {self.year}, Category: {self.category}; Cost: ${self.cost}B"


class StormNode:
    # Linked List StormNode class, very basic implementation.
    storm = False
    next = False
    prev = False

    def get_data(self):
        return self.storm

    def set_data(self, storm):
        self.storm = storm

    def set_next(self, next):
        self.next = next
    def get_next(self):
        return self.next

    def set_prev(self, prev):
        self.prev = prev

    def get_prev(self):
        return self.prev

    # I'm Lazy... convenience:
    def __init__(self,name,year,category,cost):
        self.storm = Storm(name,year,category,cost)


class StormLinkedList:
    # Actual implementation of the Double linked list methods for the StormTracker II exercise
    head = False
    tail = False
    count = 0
    def get_count(self):
        return self.count

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def get(self,i):
        # Simple double linked list logic, move to node i, then insert node s at that location in the linked list.
        if i > self.count:
            # If asking for something longer than the length of the whole list, just return the tail
            return self.tail
        else:
            # Skip to node i and insert:
            c = 1
            next = self.head
            while c < i:
                next = next.get_next()
                c += 1

            log.info(f"At the bottom of LinkedList Get, count {c}, for requested i: {i} returning node {next}.")
            return next

    def insert(self,i,s):
        # Simple double linked list logic, move to node i, then insert node s at that location in the linked list.
        if i > self.count:
            # If asking for something longer than the length of the whole list, just do a push:
            self.push(s)
        else:
            # Skip to node i and insert:
            c = 1
            next = self.head
            while c < i:
                next = next.get_next()
                c += 1
            # Now, get the next node that will become the next node -after- the inserted 's'
            curr_next = next.get_next()
            next.set_next(s)
            # Set the reverse link to the previous node:
            curr_prev = curr_next.get_prev()
            s.set_prev(curr_prev)
            s.set_next(curr_next)
            self.count += 1
        log.info(f"At the bottom of LinkedList Insert; Count: {self.count}, insert @ {i} successful.")

    def push_top(self,s):
        # Simple Linked list logic, push passed node to the top of the list:
        curr = self.head
        self.head = s
        curr.set_prev(self.head)
        self.head.set_next(curr)

        self.count += 1


    def push(self,s):
        # Simple Linked list logic, if count is 0, then head and tail must be False pointers.
        # If so, just set them both to the first (supplied) node:
        if self.count == 0:
            self.head = s
            self.tail = s

        else:
            # We're not at the start of the list, so instead of doing that, we'll link our node to the current tail node,
            # and then our current node becomes the new tail node.
            self.tail.set_next(s)
            # Now to make it a double linked list set the tail to the previous node of the new tail:
            s.set_prev(self.tail)
            # And replace the tail with the new node:
            self.tail = s
            self.tail.set_next(False)
        self.count += 1
        log.info(f"At the bottom of LinkedList Push; Count: {self.count}")


    def printForward(self):
        node = self.head
        print(node.storm)
        while (node != False):
            node = node.get_next()
            if node != False: print(node.storm)

    def printBackward(self):
        node = self.tail
        print(node.storm)
        while (node != False):
            node = node.get_prev()
            if node != False: print(node.storm)