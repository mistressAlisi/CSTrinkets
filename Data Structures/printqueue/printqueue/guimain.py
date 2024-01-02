#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ***
# printqueue/guimain.py
# CSCI211 Queue Exercise
# Last edited on 10/16/2023 by D. Mann
# ****
import logging
import time
# GUI objects:
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QTableWidgetItem,QMessageBox,QFileDialog,QDialog,QHeaderView
from gui.jobdialogue import Ui_newJobDialog

# Import main app classes:
from printqueue.classes import PrintJob,PrintJobNode,PrintQueueList
class GUIMain(QObject):
    # Variables we'll need to keep track of:
    # Our linked list/queue:
    queue = PrintQueueList()
    log = logging.getLogger(__name__)
    main_window = False
    main_widget = False

    def about(self):
        about_dialog = QMessageBox.information(self.main_widget,"About","Simple Print Queue Linked List Demo\nFall 2023  - CCP \n By D. Mann")

    def dontclickme(self):
        dcm_dialog = QMessageBox.critical(self.main_widget,"ABSOLUTE MADNESS!!","I told you to not click that button!!!!!")
        dcm_dialog = QMessageBox.critical(self.main_widget,"ABSOLUTE MADNESS!!","I really would have rather you NOT clicked that!!!!")
        dcm_dialog = QMessageBox.critical(self.main_widget,"ABSOLUTE MADNESS!!","Now you're suffering the consequences of your actions!!!!!")
        dcm_dialog = QMessageBox.critical(self.main_widget,"ABSOLUTE MADNESS!!","Don't click it again!!!!!!")

    def render_list_to_qTable(self,list,table_widget):
        # first, empty out the table:
        table_widget.setRowCount(0)
        # Now, insert every row:
        i = 0
        item = list.get_head()
        header = table_widget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        while item != False:
            # Create row:
            table_widget.insertRow(i)
            # Populate Row:
            table_widget.setItem(i, 0, QTableWidgetItem(str(item.job.id)))
            table_widget.setItem(i, 1, QTableWidgetItem(str(item.job.name)))
            table_widget.setItem(i, 2, QTableWidgetItem(str(item.job.pages)))
            table_widget.setItem(i, 3, QTableWidgetItem(str(item.job.status)))
            table_widget.setItem(i, 4, QTableWidgetItem(str(item.job.date.strftime("%D %H:%i%s"))))
            table_widget.setItem(i, 5, QTableWidgetItem(str(item.job.device)))
            # Increment counter:
            i += 1
            item = item.get_next()

    def create_queue_item(self):
        doc_name = self.diag_ui.documentName.text()
        page_count = self.diag_ui.pageCount.value()
        # Create the job:
        new_node = PrintJobNode(doc_name,page_count,"Default Device")
        # And insert it to the queue:
        self.queue.push(new_node)
        #Update GUI:
        self.update_gui()
        self.main_window.statusbar.showMessage(f"Created Queue entry for job {doc_name}")

    def get_details_diag(self):
        # Create a Dialog to ask user for queue details
        self.det_dialog = QDialog(self.main_widget)
        self.diag_ui = Ui_newJobDialog()
        self.diag_ui.setupUi(self.det_dialog)
        # Connect the handler to the button:
        self.det_dialog.accepted.connect(self.create_queue_item)
        self.det_dialog.show()

    def count_all_pages(self):
        total_pages = 0
        next = self.queue.head
        while next != False:
            total_pages += next.job.pages
            next = next.get_next()
        self.main_window.pages.display(total_pages)

    def update_gui(self):
        self.render_list_to_qTable(self.queue,self.main_window.table_step1)
        if self.queue.head:
            self.main_window.count.display(self.queue.count)
            self.count_all_pages()
        else:
            self.main_window.pages.display(0)
            self.main_window.count.display(0)

    def print_job(self):
        # Pop the top item from the queue to "print it"
        job, count = self.queue.pop()
        # if the job is false - don't overflow:
        if not job:
            self.main_window.statusbar.showMessage(f"Empty Queue! Cannot print!")
        else:
            # Easy peasy, just pop and update gui:
            self.main_window.statusbar.showMessage(f"Printed Job.")
            self.update_gui()
            print(f"Printed Job #{job.job.id}, name: {job.job.name}. Pages: {job.job.pages}")

    def add_job(self):
        self.main_window.statusbar.showMessage(f"Adding new job")
        # Ask the user for details:
        self.get_details_diag()





