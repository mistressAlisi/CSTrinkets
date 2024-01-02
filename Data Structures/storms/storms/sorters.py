#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ***
# A1_cardShuffle/cardShuffle/main.py
# CSCI211 Card Object Sorting 1 Exercise.
# Implements Sorting Algorithms.
# Last edited on 09/06/2023 by D. Mann
# ****
import logging
log = logging.getLogger(__name__)

def insertionSort(array, sort_attr="value"):
    # Insertion Sort Implementation.
    # Get len of passed array:
    alen = len(array)
    # NOTE: This insertion sort assumes an array of objects, the sort_attr param specifies the parameter to use  the sort algo.
    # Implement insertion Sort:
    i = 0
    while i < alen:
        value = array[i]
        j = i-1
        # use the chosen attribute:
        while (j >= 0) and (getattr(array[j], sort_attr) > getattr(value, sort_attr)):
            array[j+1] = array[j]
            # Decrement j:
            j -= 1
        array[j+1] = value
        # Increment i:
        i += 1
    return array


def selectionSort(array, sort_attr="value"):
    # Selection Sort Implementation.
    # Get len of passed array:
    alen = len(array)
    # NOTE: This Selection sort assumes an array of objects, the sort_attr param specifies the parameter to use  the sort algo.
    # Implement Selection Sort:
    i = 0
    while i < alen:
        smallest = i
        j = i+1
        while j < alen:
            if getattr(array[j],sort_attr) < getattr(array[smallest],sort_attr):
                smallest = j
            # Increment j:
            j += 1
        if smallest != i:
            temp = array[smallest]
            array[smallest] = array[i]
            array[i] = temp
        # Increment i:
        i += 1
    return array


def countSort(array, sort_attr="value"):
    # Count Sort Implementation.
    # Get len of passed array:
    alen = len(array)
    # Temporary data array:
    ret_array = array

    # Find maximum in current array:
    amax = getattr(array[0],sort_attr)
    for item in array:
        cmax = getattr(item,sort_attr)
        if cmax > amax:
            amax = cmax

    #Initialize the counting array:
    count_array = [0]*(amax+1)

    # For each value in array, increment the corresponding index in count_array:
    for item in array:
        value = getattr(item,sort_attr)
        count_array[value] += 1

    log.info(f"Counting Array at init:\n{count_array}")

    # Do a linear sum of values in count_array:
    for i in range(1,amax+1,1):
        count_array[i] += count_array[i-1]

    log.info(f"Counting Array post-linear:\n{count_array}")

    # For each value in array, decrease value in count_array and put the value in the temporary array:
    for i in range(0,amax,1):
        temp = array[i]
        key = getattr(temp, sort_attr)
        count_array[key] -= 1
        ret_array[key] = temp

    log.info(f"Counting Array post-linear:\n{count_array}")
    log.info(f"Return Array post-linear:\n{ret_array}")
    # Copy the array back and return it:
    for i in range(0, amax, 1):
        array[i] = ret_array[i]
    return ret_array





def mergeSort(array, sort_attr):
    # MergeSort implementation:
    # Check boundary:
    arrsize = len(array)
    if arrsize > 1:
        # Middle index: Take modulo 2 to get an integer:
        middle = arrsize //2
        # Now in the classic pythonic manner, use the [a:b] operator to slice the array:
        # First, the left half up to middle:
        left_array = array[:middle]
        # Then, the right half from middle to end:
        right_array = array[middle:]

        # Note, this is a recursive array, the function will call itself for each half progressively:
        mergeSort(left_array, sort_attr)
        mergeSort(right_array, sort_attr)

        # Now, we need some counters for the fun:
        # Lower/left counter:
        lc = 0
        # Upper/right counter:
        rc = 0
        # Global counter:
        i = 0

        # Let's get the array lengths:
        left_size = len(left_array)
        right_size = len(right_array)
        # Now, operate on the two halves of the array and merge the values back recursively on to the main array:
        while lc < left_size and rc < right_size:
            # Now, compare the values present in the arrays at lc and uc, and merge
            # only the largest value into the main array.
            # Bear in mind we're using the sort_attr parameter here:
            lv = getattr(left_array[lc], sort_attr)
            rv = getattr(right_array[rc], sort_attr)
            # Compare values:
            if lv < rv:
                # LEFT is smaller than RIGHT - Copy Left:
                array[i] = left_array[lc]
                # Step through array:
                lc += 1
            else:
                # RIGHT is smaller than LEFT - Copy Right:
                array[i] = right_array[rc]
                rc += 1
            # Increase global counter:
            i += 1

        # Make sure all values from the left array are merged:
        while lc < left_size:
            array[i] = left_array[lc]
            lc += 1
            i += 1

        # Make sure all values from the right array are merged:
        while rc < right_size:
            array[i] = right_array[rc]
            rc += 1
            i += 1

    return array




def quickSort(array,sort_attr,start,end):
    # QuickSort Implementation:
    # Count variables:
    lc = start
    uc = end
    # We're at the bottom of the recursion, exit the loop:
    # if end > start:
    #     return array
    # Middle index: Take middle of array
    pivot_key = int((lc+uc)/2)
    log.info(f"Pivot: Key: {pivot_key}")
    # Take pivot value:
    pivot = getattr(array[pivot_key],sort_attr)
    log.info(f"Pivot Value: {pivot} ")
    # Implement partitioning: Move numbers around to the right partitions:
    while lc <= uc:
        log.info(f"LC: {lc}, UC: {uc}, {getattr(array[lc],sort_attr)}, {pivot}")
        while getattr(array[lc],sort_attr) < pivot:
            # Increment lower insert index while values are less than pivot:
            log.info(f"LCD {lc}")
            lc += 1
        while getattr(array[uc],sort_attr) > pivot:
            # Decrement the upper insert index while values are greater than pivot:
            log.info(f"UCD {uc}")
            uc -= 1
        if lc <= uc:
            # Swap elements around lc and uc:
            # The most  pythonic is the double assignment swap, it needs no temp variable!
            array[lc], array[uc] = array[uc], array[lc]
            lc += 1
            uc -= 1

    # Recursively partition and quicksort:
    if start < uc:
        quickSort(array,sort_attr,start,uc)
    if lc < end:
        quickSort(array,sort_attr,lc,end)

    return array


