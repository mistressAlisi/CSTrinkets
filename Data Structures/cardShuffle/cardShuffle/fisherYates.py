#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ***
# A1_cardShuffle/cardShuffle/main.py
# CSCI211 Card Object Sorting 1 Exercise.
# Implements Fisher-Yates Pseudorandom Algorithm
# Last edited on 09/06/2023 by D. Mann
# ****

import time
import random


def shuffle(array):
    # Seed Random number generator:
    random.seed(time.mktime(time.localtime()))
    # Get len of passed array:
    alen = len(array)

    # Implement Fisher-Yates:
    i = 0
    while i < alen:
        # Randint to 2^32:
        j = random.randint(0,2**32) % (i+1)
        # Randomize Array:
        curr_item = array[j]
        array[j] = array[i]
        array[i] = curr_item
        # Increment i:
        i += 1
    # Return pseudo-randomised array:
    return array
