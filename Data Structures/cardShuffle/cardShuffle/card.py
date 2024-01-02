#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ***
# A1_cardShuffle/cardShuffle/main.py
# CSCI211 Card Object Sorting 1 Exercise.
# Card Class
# Last edited on 09/06/2023 by D. Mann
# ****
from cardShuffle import constants


class Card:

    value = 0
    suit = 0

    def __init__(self, value=0, suit=0):
        # Let's start by copying the value and suit assigned to this instance into the class variables:
        self.value = value
        self.suit = suit

    # For convenience's sake, in case we need to print the card:
    def __str__(self):
        return f"Card Instance, Value: {constants.CARD_VALUES[self.value]}, Suit: {constants.CARD_SUITS[self.suit]}"