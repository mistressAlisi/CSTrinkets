#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ***
# A1_cardShuffle/cardShuffle/main.py
# CSCI211 Card Object Sorting 1 Exercise.
# Main driver Code
# Last edited on 09/06/2023 by D. Mann
# ****
import time
import logging
# import our Card class:
from cardShuffle.card import Card
# And Fisher-Yates:
from cardShuffle.fisherYates import shuffle

# Sorters:
from cardShuffle.sorters import insertionSort
from cardShuffle.sorters import selectionSort
from cardShuffle.sorters import mergeSort
from cardShuffle.sorters import quickSort
# Suits and Values:
from cardShuffle import constants


# Prints an array of cards as a V - S string:
def print_card_array(array):
    for item in array:
        print(f"{constants.CARD_VALUES[item.value]} - {constants.CARD_SUITS[item.suit]}")


def main_a1():
    log = logging.getLogger(__name__)

    # Initialize the array to implement Fisher-Yates:
    cards = []
    # Fastest way to iterate through these hashes to create a 2D array is to use two for... statements using the hash indices:
    count = 0
    # Performance counters:
    time_p0 = time.perf_counter()
    print("Step 1: Create and populate card Array...")
    # [v] for values, [s] for suits:
    for v in constants.CARD_VALUES:
        for s in constants.CARD_SUITS:
            log.info(f"Creating Card {constants.CARD_SUITS[s]}.{constants.CARD_VALUES[v]}...")
            # Create instance of Card and append to array for Fisher-Yates:
            cards.append(Card(v, s))
            count += 1
    log.info(f"Created {count} cards.")
    print(f"...Created {count} cards:")
    print_card_array(cards)

    time_p1 = time.perf_counter()
    print ("Step 2: Shuffle it with Fisher-Yates...")
    # Shuffle and proof:
    shuffled_cards = shuffle(cards)
    print_card_array(shuffled_cards)

    time_p2 = time.perf_counter()
    print ("Step 3: Insertion sort on value of cards....")
    # insertionSort and proof:
    sorted_first = insertionSort(shuffled_cards,"value")
    print_card_array(sorted_first)

    time_p3 = time.perf_counter()
    print ("Step 4: Selection sort on value, and insertion on suit of cards....")
    # Selection, then Insertion sort, and proof:
    sorted_next = selectionSort(shuffled_cards,"value")
    final_sort = insertionSort(sorted_next,"suit")
    print_card_array(final_sort)

    time_p4 = time.perf_counter()
    time_EP = time_p4-time_p0
    log.info(f"Performance Counters:\nTotal Time:{time_EP}s.\nCreate and Populate: {time_p1-time_p0}s.\nShuffle: {time_p2-time_p1}s.\nInsertion Sort: {time_p3-time_p2}s.\nInsert and Select Sort: {time_p4-time_p3}s.")


def main_a2():
    log = logging.getLogger(__name__)

    # Initialize the array to implement Fisher-Yates:
    cards = []
    # Fastest way to iterate through these hashes to create a 2D array is to use two for... statements using the hash indices:
    count = 0
    # Performance counters:
    time_p0 = time.perf_counter()
    print("Step 1: Create and populate card Array...")
    # [v] for values, [s] for suits:
    for v in constants.CARD_VALUES:
        for s in constants.CARD_SUITS:
            log.info(f"Creating Card {constants.CARD_SUITS[s]}.{constants.CARD_VALUES[v]}...")
            # Create instance of Card and append to array for Fisher-Yates:
            cards.append(Card(v, s))
            count += 1
    log.info(f"Created {count} cards.")
    print(f"...Created {count} cards:")
    print_card_array(cards)

    time_p1 = time.perf_counter()
    print ("Step 2: Shuffle it with Fisher-Yates...")
    # Shuffle and proof:
    shuffled_cards = shuffle(cards)
    print_card_array(shuffled_cards)

    time_p2 = time.perf_counter()
    print ("Step 3: Quicksort sort on value of cards....")
    # insertionSort and proof:
    sorted_first = quickSort(shuffled_cards,"value",0,count-1)
    print_card_array(sorted_first)

    time_p3 = time.perf_counter()
    print ("Step 4: Quick sort on value, and merge sort on suit of cards....")
    # Selection, then Insertion sort, and proof:
    sorted_next = quickSort(shuffled_cards,"value",0,count-1)
    final_sort = mergeSort(sorted_next[::-1],"suit")
    print_card_array(final_sort)

    time_p4 = time.perf_counter()
    time_EP = time_p4-time_p0
    log.info(f"Performance Counters:\nTotal Time:{time_EP}s.\nCreate and Populate: {time_p1-time_p0}s.\nShuffle: {time_p2-time_p1}s.\nQuick Sort: {time_p3-time_p2}s.\nQuick and Merge Sort: {time_p4-time_p3}s.")
