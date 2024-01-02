#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ***
# stormtracker/main.py
# CSCI211 Fire Station Linked List Exercise
# Last edited on 10/03/2023 by D. Mann
# ****
# Classes we're going to need, Storms and Nodes for Linked Lists.
# Libraries we need:
import logging,sys,argparse
log = logging.getLogger(__name__)


class FireStation:
    # Actual class describing the storm data for FireStation.
    location = ""
    number = 1

    def __init__(self,number,location):
        self.location = location
        self.number = number

    def get_station_number(self):
        return self.number

    def __str__(self):
        return f"Fire Station #{self.number}, location: {self.location}"



class FireStationNode:
    # Linked List FireStation class, very basic implementation.
    station = False
    # Next and Previous pointers:
    next = False
    prev = False
    def set_station(self,station):
        self.station = station

    def set_data(self, station):
        self.station = station

    def get_station(self):
        return self.station

    def get_data(self):
        return self.station

    def set_next(self, next):
        self.next = next

    def set_prev(self, prev):
        self.prev = prev

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    # I'm Lazy... convenience:
    def __init__(self,name,location):
        self.station = FireStation(name,location)


class StationLinkedList:
    # Actual implementation of the Double linked list methods for the Firestation exercise
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
            c = 0
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
            c = 0
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
            # Now to make it a double linked list set the tail to the previous node of the new tail:
            s.set_prev(self.tail)
            # And replace the tail with the new node:
            self.tail = s
            self.tail.set_next(False)
            self.count += 1
        log.info(f"At the bottom of LinkedList Push; Count: {self.count}")


    def printForward(self):
        node = self.head
        print(node.station)
        while (node != False):
            node = node.get_next()
            if node != False: print(node.station)

    def printBackward(self):
        node = self.tail
        print(node.station)
        while (node != False):
            node = node.get_prev()
            if node != False: print(node.station)