#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ***
# A1_cardShuffle/main.py
# CSCI211 Card Object Sorting 1 and 2 Exercises GUI.
# Last edited on 09/13/2023 by D. Mann
# ****
# Libraries we need:
import logging,sys,argparse
# Importing stuff for UI:
import sys
from PyQt5.QtWidgets import QApplication,QDialog,QMainWindow
from gui.cardshuffle_mw import Ui_CardShuffleMW

#Import main application:
from cardShuffle.guimain import GUIMain

# Declare arguments:
args = argparse.ArgumentParser()
args.add_argument("-d","--debug",help="Enable Debugging.",const=logging.DEBUG,action="store_const",dest="logging")
args.add_argument("-a","--about",help="Print about and Exit",const=True,action="store_const",dest="about")
parsed_args = args.parse_args()

logging.basicConfig(level=parsed_args.logging)
if __name__ == '__main__':
    if parsed_args.about == True:
        # Print version and exit.
        print("CardShuffle, V1.0. CSCI211 Card Object Sorting GUI Exercise by D. Mann");
        sys.exit()

    # Create UI, load window code gui from package and connect signals and slots:
    # Application first:
    app = QApplication(sys.argv)
    # Window Next:
    window = QMainWindow()
    # Instantiate and bind UI definition to Window -
    ui = Ui_CardShuffleMW()
    ui.setupUi(window)
    # Load our Main Application code next, we will be connecting it's signals to the UI app:
    # Pass it the window pointer so it can modify contents:
    main = GUIMain()
    main.main_window = ui
    main.main_widget = window
    # Setup combo boxes:
    main.poppulate_combo_boxes()

    # Connect SIGNALS now:
    # ShuffleBtn connects to the Shuffle function in the main app!
    ui.shuffleBtn.clicked.connect(main.shuffle_all_steps)
    # Connect About signal:
    ui.actionAboutProj.triggered.connect(main.about)
    # Another fun signal:
    ui.actionDontClick.triggered.connect(main.dontclickme)
    # Last signaL
    ui.actionShuffle.triggered.connect(main.shuffle_all_steps)
    # And bob's your uncle; Open for business!
    window.show()
    sys.exit(app.exec_())
