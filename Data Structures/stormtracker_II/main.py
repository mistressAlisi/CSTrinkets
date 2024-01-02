#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ***
# main.py
# CSCI211 Stormtracker Linked List Exercise
# Last edited on 10/09/2023 by D. Mann
# ****
# Libraries we need:
import logging,sys,argparse



# Declare arguments:
args = argparse.ArgumentParser()
args.add_argument("-d","--debug",help="Enable Debugging.",const=logging.DEBUG,action="store_const",dest="logging")
args.add_argument("-a","--about",help="Print about and Exit",const=True,action="store_const",dest="about")
args.add_argument("file",help="Specify CSV File to operate on",type=argparse.FileType('r'))
parsed_args = args.parse_args()

logging.basicConfig(level=parsed_args.logging)

# Import main driver code:
from stormtracker.main import main

if __name__ == '__main__':
    if parsed_args.file == None:
        print("Error! You need to specify a CSV file.");
        sys.exit(1)
    if parsed_args.about == True:
        # Print version and exit.
        print("StormTracker, V1.0. CSCI211 Linked List Exercise  by D. Mann");
        sys.exit()
    with parsed_args.file as file:
        logging.info(f"CSV Source file: {file.name}")
        main(file)
        file.close()
    sys.exit()