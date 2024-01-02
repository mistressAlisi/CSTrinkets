#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ***
# main.py
# CSCI211: Pathfinder: Djikstra vs Kruskal program
# Last edited on 11/12/2023 by D. Mann
# ****
# Libraries we need:
import logging,sys,argparse,os
from pathfinder.dijkstra import Dijkstra

# Declare arguments:
args = argparse.ArgumentParser()
args.add_argument("-d","--debug",help="Enable Debugging.",const=logging.DEBUG,action="store_const",dest="logging")
args.add_argument("-a","--about",help="Print about and Exit",const=True,action="store_const",dest="about")

parsed_args = args.parse_args()

logging.basicConfig(level=parsed_args.logging)

# Import main driver code:
from pathfinder.main import main

if __name__ == '__main__':
    if parsed_args.about == True:
        # Print version and exit.
        print("Pathfinder, V1.0. CSCI211 Dijkstra/Kruskal Exercise  by D. Mann");
        sys.exit()
    main()
    sys.exit()
