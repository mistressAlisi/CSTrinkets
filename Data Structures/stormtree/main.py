#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ***
# main.py
# CSCI211: StormTree: Storm BST Exercise
# Last edited on 06/11/2023 by D. Mann
# ****
# Libraries we need:
import logging,sys,argparse



# Declare arguments:
args = argparse.ArgumentParser()
args.add_argument("-d","--debug",help="Enable Debugging.",const=logging.DEBUG,action="store_const",dest="logging")
args.add_argument("-a","--about",help="Print about and Exit",const=True,action="store_const",dest="about")
args.add_argument("file",help="Specify CSV File to operate on",type=argparse.FileType('r'))
# args.add_argument("attr",help="Attribute or Column to use as ordering col for Tree Operation")
# args.add_argument("prefix",help="Prefix for neato/dot file(s) to be generated.")
parsed_args = args.parse_args()

logging.basicConfig(level=parsed_args.logging)

# Import main driver code:
from stormtree.main import main

if __name__ == '__main__':
    if parsed_args.file == None:
        print("Error! You need to specify a CSV file.");
        sys.exit(1)
    if parsed_args.about == True:
        # Print version and exit.
        print("StormTree, V1.0. CSCI211 BST Exercise  by D. Mann");
        sys.exit()
    with parsed_args.file as file:
        logging.info(f"CSV Source file: {file.name}")
        main(file)
        file.close()
    sys.exit()