#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ***
# main.py
# CSCI211 HashMagic Hashing Exercise Example
# Last edited on 10/23/2023 by D. Mann
# ****
# Libraries we need:
import logging,sys,argparse,csv

# Random? Random. Numpy Random. Numpy Unique too. :D
import numpy as np


# Declare arguments:
args = argparse.ArgumentParser()
args.add_argument("-d","--debug",help="Enable Debugging.",const=logging.DEBUG,action="store_const",dest="logging")
args.add_argument("-a","--about",help="Print about and Exit",const=True,action="store_const",dest="about")
parsed_args = args.parse_args()

logging.basicConfig(level=parsed_args.logging)
log = logging.getLogger(__name__)
# Example Hashing function, demonstrated in lecture slides:
def hashify(data,keysize):
    hash = 0
    for c in bytes(data,'utf8'):
        hash += int(c)
    return hash % keysize

# Second example: Hashify prime by using a prime factor to do 1d multiply:
def hashify_prime(data,keysize,factor=19):
    hash = 0
    for c in bytes(data,'utf8'):
        hash = (factor * hash) + int(c)
        #hash += int.from_bytes(cb, sys.byteorder)
    return hash % keysize

# PolyPrime or Prime-Plus hashing relying on second order polynomials:
def hashify_poly_prime(data,keysize):
    # Polynomial Hash Algorithm relying on a small<->large relationship, A and B:
    # WE KNOW JNumbers are a string and an int; so we discard the J, and just take the int:
    # Data = int(data[1:])
    # A is optimised to 263. B is optimised to 1000000007
    A = 263
    B = 1000000007
    # Formula is (data * A) % B
    lhash = 0
    lhash += (int(data[1:]*1)*A) % B
    return lhash % keysize
def print_perf(array_size,key_size,key_array,algo_name="default"):
    print(f"***Hash Function {algo_name}***")
    print(f"**Hash Perf Overview @ keysize: {key_size} for Array size {array_size}:")
    # Python+NumPy is the bee's knees:
    # Calculate the Collisions, no-match and no_collision counts for array performance:
    collisions = 0
    no_collision = 0
    no_match = 0
    #print(key_array)
    for hash_key in key_array.keys():
        hash_count = int(key_array[hash_key])

        if hash_count == 0:
            # If count is zero, there are no matches:
            no_match += 1
            no_collision += 1
            log.info(f"Hash Key: {hash_key}, no values!")
        elif hash_count == 1:
            # Hash count = 1 - no collision:
            log.info(f"Hash Key: {hash_key}, no collisions! ")
        elif hash_count > 1:
            # If hash_count > 1, then we have (a) collision(s):
            log.info(f"Hash Key {hash_key} has {hash_count} collisions.")
            collisions += hash_count
        no_collision = array_size - collisions


    print(f"*** Total Hash function Performance: Total Collision count: {collisions} No Match: {no_match}. No Collisions: {no_collision}")
    if collisions >0 and no_collision > 0:
         print(f"\n**Collision to No-collision ratio: {no_collision/collisions}**\n")
    if no_match >0:
        print(f"\n**Coverage - No-Match/Keysize ratio: {(no_match/key_size)}**\n")


if __name__ == '__main__':
    if parsed_args.about == True:
        # Print version and exit.
        print("Classic Modulo Hash Tester, V1.0. CSCI211  by D. Mann");
        sys.exit()
    data_array = []

    rng = np.random.default_rng()
    # Generate an array of 25,000 correctly formatted J-Numbers and a source dict to copy for storage structs:
    log.info("Generating 25000 Random J-numbers....")
    print("Randomly generating J-Numbers...")
    data_array = [f"J{x:08}" for x in rng.integers('1', '99999999', size=25000, endpoint=True)]

    # Compute perf for different sizes and algos
    #for array_size,key_size in [(20,10),(40,20)]:
    for array_size,key_size in [(20,10),(10,20),(100,127),(500,512),(1000,1024),(25000,27000)]:
        # Initialize dicts:
        def_dict = {}
        prime_dict = {}
        pprime_dict = {}
        for i in range (0,key_size,1):
            def_dict[i] = 0
            prime_dict[i] = 0
            pprime_dict[i] = 0
        # Run Hash functions and collect results:
        for value in data_array[0:array_size]:
            hashed = hashify(value,key_size)
            primehash = hashify_prime(value,key_size)
            pphash = hashify_poly_prime(value,key_size)
            log.info(f"Value {value} hashes to {hashed}. Primehashes to: {primehash}, Prime Poly Hash: {pphash}")
            def_dict[hashed] += 1
            prime_dict[primehash] += 1
            pprime_dict[pphash] += 1
        # Finally, report back to the user:
        print_perf(array_size,key_size,def_dict,"~~Default Hash~~")
        print_perf(array_size, key_size, prime_dict,"~~Prime Hash~~")
        print_perf(array_size, key_size, pprime_dict, "~~Poly Prime Hash~~")

    sys.exit()

