#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ***
# main.py
# CSCI211 HashMagic Hashing Exercise Random J number generator
# Last edited on 10/23/2023 by D. Mann
# ****
# Libraries we need:
import logging,sys,argparse,csv

# Random? Random. Numpy Random.
import numpy as np


# Declare arguments:
args = argparse.ArgumentParser()
args.add_argument("-d","--debug",help="Enable Debugging.",const=logging.DEBUG,action="store_const",dest="logging")
args.add_argument("-a","--about",help="Print about and Exit",const=True,action="store_const",dest="about")
args.add_argument("file",help="Specify File to generate",type=argparse.FileType('w'))
args.add_argument("count",help="Specify Count of Random Jnumbers to generate",type=int)
parsed_args = args.parse_args()

logging.basicConfig(level=parsed_args.logging)



if __name__ == '__main__':
    if parsed_args.file == None:
        print("Error! You need to specify a CSV file.");
        sys.exit(1)
    if parsed_args.count == None:
        print("Error! You need to specify a Count.");
        sys.exit(1)
    if parsed_args.about == True:
        # Print version and exit.
        print("Random JNumber Generator, V1.0. CSCI211  by D. Mann");
        sys.exit()
    with parsed_args.file as file:
        logging.info(f"Destination file: {file.name} - count: {parsed_args.count}")
        csvwriter = csv.writer(parsed_args.file)
        csvwriter.writerow(['count','jnumber'])
        rng = np.random.default_rng()
        for i in range(0,parsed_args.count,1):
            rand = rng.integers('10000000','99999999',size=1,endpoint=True)
            csvwriter.writerow([i, f'J{rand[0]}'])
            logging.info(f"Generated JNumber: J{rand[0]}")
        file.close()
    sys.exit()