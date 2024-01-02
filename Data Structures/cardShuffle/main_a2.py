#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ***
# A1_cardShuffle/main.py
# CSCI211 Card Object Sorting 1 Exercise.
# Last edited on 09/06/2023 by D. Mann
# ****
# Libraries we need:
import logging,sys,argparse



# Declare arguments:
args = argparse.ArgumentParser()
args.add_argument("-d","--debug",help="Enable Debugging.",const=logging.DEBUG,action="store_const",dest="logging")
args.add_argument("-a","--about",help="Print about and Exit",const=True,action="store_const",dest="about")
parsed_args = args.parse_args()

logging.basicConfig(level=parsed_args.logging)

# Import main driver code:
from cardShuffle import main

if __name__ == '__main__':
    if parsed_args.about == True:
        # Print version and exit.
        print("CardShuffle, V1.0. CSCI211 Card Object Sorting Exercise 2  by D. Mann");
        sys.exit()
    sys.exit(main.main_a2())