#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ***
# gui_main/printqueue.py
# CSCI211 Print Queue Station Linked List Exercise
# Last edited on 10/16/2023 by D. Mann
# ****
# Libraries we need:
import logging,sys,argparse
# Importing stuff for UI:
import sys
from PyQt5.QtWidgets import QApplication,QDialog,QMainWindow
from gui.printqueue_mw import Ui_PrinterQueue_mw

#Import main application:
from printqueue.guimain import GUIMain


# Declare arguments:
args = argparse.ArgumentParser()
args.add_argument("-d","--debug",help="Enable Debugging.",const=logging.DEBUG,action="store_const",dest="logging")
args.add_argument("-a","--about",help="Print about and Exit",const=True,action="store_const",dest="about")
parsed_args = args.parse_args()

logging.basicConfig(level=parsed_args.logging)
if __name__ == '__main__':
    if parsed_args.about == True:
        # Print version and exit.
        print("Print Queue Demo, V1.0. CSCI211 Linked List Object Sorting GUI Exercise by D. Mann");
        sys.exit()

    # Create UI, load window code gui from package and connect signals and slots:
    # Application first:
    app = QApplication(sys.argv)
    # Window Next:
    window = QMainWindow()
    # Instantiate and bind UI definition to Window -
    ui = Ui_PrinterQueue_mw()
    ui.setupUi(window)
    # Load our Main Application code next, we will be connecting it's signals to the UI app:
    # Pass it the window pointer so it can modify contents:
    main = GUIMain()
    main.main_window = ui
    main.main_widget = window
    # Setup combo boxes:

    # # Connect About signal:
    ui.actionAboutProj.triggered.connect(main.about)
    # # Another fun signal:
    ui.actionDontClick.triggered.connect(main.dontclickme)
    # # Last signals
    ui.printBtn.clicked.connect(main.print_job)
    ui.addBtn.clicked.connect(main.add_job)
    # And bob's your uncle; Open for business!
    window.show()
    sys.exit(app.exec_())
