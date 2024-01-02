#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ***
# firestation/main.py
# CSCI211 Fire Station Linked List Exercise
# Last edited on 10/03/2023 by D. Mann
# ****
# Libraries we need:
import logging,sys,argparse
# Importing stuff for UI:
import sys
from PyQt5.QtWidgets import QApplication,QDialog,QMainWindow
from gui.stormtracker_mw import Ui_StormTrackerMW

#Import main application:
from stormtracker.guimain import GUIMain

# Declare arguments:
args = argparse.ArgumentParser()
args.add_argument("-d","--debug",help="Enable Debugging.",const=logging.DEBUG,action="store_const",dest="logging")
args.add_argument("-a","--about",help="Print about and Exit",const=True,action="store_const",dest="about")
parsed_args = args.parse_args()

logging.basicConfig(level=parsed_args.logging)
if __name__ == '__main__':
    if parsed_args.about == True:
        # Print version and exit.
        print("Stormtracker Demo, V1.0. CSCI211 Linked List Object Sorting GUI Exercise by D. Mann");
        sys.exit()

    # Create UI, load window code gui from package and connect signals and slots:
    # Application first:
    app = QApplication(sys.argv)
    # Window Next:
    window = QMainWindow()
    # Instantiate and bind UI definition to Window -
    ui = Ui_StormTrackerMW()
    ui.setupUi(window)
    # Load our Main Application code next, we will be connecting it's signals to the UI app:
    # Pass it the window pointer so it can modify contents:
    main = GUIMain()
    main.main_window = ui
    main.main_widget = window
    # Setup combo boxes:
    main.poppulate_combo_boxes()

    # # Connect SIGNALS now:
    # # ShuffleBtn connects to the Shuffle function in the main app!
    ui.runBtn.clicked.connect(main.list_all_steps)
    # # Connect About signal:
    ui.actionAboutProj.triggered.connect(main.about)
    # # Another fun signal:
    ui.actionDontClick.triggered.connect(main.dontclickme)
    # # Last signaL
    ui.actionLoad.triggered.connect(main.list_all_steps)
    # And bob's your uncle; Open for business!
    window.show()
    sys.exit(app.exec_())
