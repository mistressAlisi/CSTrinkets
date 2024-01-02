#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ***
# A1_cardShuffle/cardShuffle/main.py
# CSCI211 Card Object Sorting 1 Exercise.
# Constants.
# Last edited on 09/06/2023 by D. Mann
# ****
# Dicts (hashes) make more sense for Values and suits, since the value range is 2-10+J,Q,K,A, we'll define it as a hash table from 0 through 12, respectively, using integer keys:
# Integer keys also store the values in sequence. Useful for Sorting later:
CARD_VALUES = {
    0: "2",
    1: "3",
    2: "4",
    3: "5",
    4: "6",
    5: "7",
    6: "8",
    7: "9",
    8: "10",
    9: "J",
    10: "Q",
    11: "K",
    12: "A"
}

# Same for the Suit:
CARD_SUITS = {
    0: "C",
    1: "D",
    2: "H",
    3: "S"
}