#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ***
# printqueue/classes.py
# CSCI211 Queue Exercise
# Last edited on 10/16/2023 by D. Mann
# ****
# Classes we're going to need, PrintJob and Nodes for Linked List Queues
# Libraries we need:
import logging,sys,argparse,datetime
log = logging.getLogger(__name__)


class PrintJob:
    # Actual class describing the storm data for FireStation.
    id = 0
    name = ""
    pages = 1
    device = ""
    status = "SUBMITTED"
    date = False
    def __init__(self,name,pages,device):
        self.name = name
        self.pages = pages
        self.device = device
        self.date = datetime.datetime.now()

    def get_id(self):
        return self.id

    def set_id(self,id):
        self.id = id
        return self.id

    def __str__(self):
        return f"Job #{self.id}, Title: {self.name}, Pages: {self.pages}"



class PrintJobNode:
    # Linked List FireStation class, very basic implementation.
    job = False
    # Next and Previous pointers:
    next = False
    prev = False

    def set_job(self,job):
        self.job = job

    def set_data(self,job):
        self.job = job

    def get_job(self):
        return self.job

    def get_data(self):
        return self.job

    def set_next(self, next):
        self.next = next

    def set_prev(self, prev):
        self.prev = prev

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    # I'm Lazy... convenience:
    def __init__(self,name,pages,device):
        self.job = PrintJob(name,pages,device)


class PrintQueueList:
    # Actual implementation of the Double linked list methods for the Queue exercise
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
        # Simple double linked list logic, move to node i, and return the desired node
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



    def push(self,s):
        # Simple Linked list queue logic, if count is 0, then head and tail must be False pointers.
        # If so, just set them both to the first (supplied) node:
        if self.count == 0:
            self.head = s
            self.tail = s
            self.count += 1
        else:
            # We're not at the start of the list, so instead of doing that, we'll link our node to the current tail node,
            # and then our current node becomes the new tail node; linked to the old tail node.
            self.tail.set_next(s)
            # Now to make it a double linked list set the tail to the previous node of the new tail:
            s.set_prev(self.tail)
            # And replace the tail with the new node:
            self.tail = s
            self.tail.set_next(False)
            self.count += 1
        # The item needs to get the id assigned:
        s.job.set_id(self.count)
        log.info(f"At the bottom of Queue Push; Count: {self.count}")


    def pop(self):
        # Get current head, reduce count by 1, and set the next node from the current head to be the new head
        if self.count == 0:
            #  Empty queue! - do not die on us:
           return False,0
        log.info(f"At the top of Queue Pop; Count: {self.count}, job: {self.head.job}")
        chead = self.head
        self.head = chead.get_next()
        self.count -= 1
        return chead, self.count

    def printForward(self):
        node = self.head
        print(node.job)
        while (node != False):
            node = node.get_next()
            if node != False: print(node.job)

    def printBackward(self):
        node = self.tail
        print(node.job)
        while (node != False):
            node = node.get_prev()
            if node != False: print(node.job)