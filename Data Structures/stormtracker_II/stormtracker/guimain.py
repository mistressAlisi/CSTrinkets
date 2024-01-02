import logging
import time
import csv
# GUI objects:
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QTableWidgetItem,QMessageBox,QFileDialog,QHeaderView


# import our Data struct classes:
from stormtracker.classes import Storm,StormNode,StormLinkedList


class GUIMain(QObject):
    # Variables we'll need to keep track of:
    # Our linked list:
    linked_list = StormLinkedList()
    log = logging.getLogger(__name__)
    main_window = False
    main_widget = False

    def about(self):
        about_dialog = QMessageBox.information(self.main_widget,"About","Stormtracker: Storm Linked List Demo\nFall 2023  - CCP \n By D. Mann")

    def dontclickme(self):
        dcm_dialog = QMessageBox.critical(self.main_widget,"ABSOLUTE MADNESS!!","I told you to not click that button!!!!!")
        dcm_dialog = QMessageBox.critical(self.main_widget,"ABSOLUTE MADNESS!!","I really would have rather you NOT clicked that!!!!")
        dcm_dialog = QMessageBox.critical(self.main_widget,"ABSOLUTE MADNESS!!","Now you're suffering the consequences of your actions!!!!!")
        dcm_dialog = QMessageBox.critical(self.main_widget,"ABSOLUTE MADNESS!!","Don't click it again!!!!!!")

    def open_file_name_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None, "Select Data Source", "./","CSV-Formatted Data (*.csv)", options=options)
        return fileName


    def poppulate_combo_boxes(self):
        # Only call this function once during gui creation to setup the Combo Boxes. Call it after main window is set!

        # Populate algorithm selectors:
        self.main_window.sort1.clear()
        for k,v in [
            #("i","Insert Sort"),
            #("s","Selection Sort"),
            # ("c","Count Sort"),
            #("m","Merge Sort"),
            ("q","Quicksort")]:
            self.main_window.sort1.addItem(v,k)
            # self.main_window.sort2.addItem(v,k)



    def render_list_to_qTable(self,list,table_widget):
        # first, empty out the table:
        table_widget.setRowCount(0)
        # Now, insert every row:
        i = 0
        item = list.get_head()
        while item != False:
            # Create row:
            table_widget.insertRow(i)
            # Populate Row:
            table_widget.setItem(i, 0, QTableWidgetItem(str(item.storm.__str__())))
            # Increment counter:
            i += 1
            item = item.get_next()

    def render_list_to_qTable_backwards(self,list,table_widget):
        # first, empty out the table:
        table_widget.setRowCount(0)
        # Now, insert every row:
        i = 0
        item = list.get_tail()
        while item != False:
            # Create row:
            table_widget.insertRow(i)
            # Populate Row:
            table_widget.setItem(i, 0, QTableWidgetItem(str(item.storm.__str__())))
            # Increment counter:
            i += 1
            item = item.get_prev()

    def render_array_to_qTable(self,array,table_widget):
        # first, empty out the table:
        table_widget.setRowCount(0)
        # Now, insert every row:
        i = 0
        for item in array:
            # Create row:
            table_widget.insertRow(i)
            # Populate Row:
            if item[2] == 0:
                table_widget.setItem(i, 0, QTableWidgetItem(f"Tropical Storm {item[0]}, year: {item[1]}, Cost: ${item[3]}B"))
            else:
                table_widget.setItem(i, 0, QTableWidgetItem(f"Hurricane {item[0]} (category {item[2]}), year: {item[1]}, Cost: ${item[3]}B"))
            # Increment counter:
            i += 1


    def parse_csv(self,file):
        csvreader = csv.reader(file)
        # skip header:
        csvreader.__next__()
        # return an array, for convenience later during sorting. We create the linked list mostly for
        # rendering purposes.
        entry_array = []
        for storm_row in csvreader:
            # Create a Storm Linked list and Node instance for each row:
            self.log.info(f"Creating a new node for Storm {storm_row}")
            entry_array.append([storm_row[0],int(storm_row[1]),int(storm_row[2]),storm_row[3]])
        return entry_array

    def list_all_steps(self):
        # Step 1: Select file:
        csv_file = self.open_file_name_dialog()
        # Now open and parse it:
        time_p0 = time.perf_counter_ns()
        self.log.debug(f"Source File: {csv_file}")
        with open(csv_file,"r") as open_file:
            entry_array = self.parse_csv(open_file)
            open_file.close()

        time_p1 = time.perf_counter_ns()
        # And it's perf counter:
        time_p1t = time_p1 - time_p0
        # Update gui:
        self.log.debug(f"Phase P1: Perf Counter: {time_p1t}")
        header = self.main_window.table_step1.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.render_array_to_qTable(entry_array,self.main_window.table_step1)

        self.main_window.time_p1.display(str(time_p1t))
        # Step 2: Let's sort the contents: [0:14] will be pushed to a new list,
        # Then [15:29] to the top of the list, and
        # Finally [:30] to the position [14] in the new list.
        self.log.info("Step 2: Execute 'Sort'")
        time_p1 = time.perf_counter_ns()
        # 0 to 14:
        for storm_row in entry_array[0:14]:
            self.log.info(storm_row)
            nst = StormNode(storm_row[0], storm_row[1], storm_row[2], storm_row[3])
            self.linked_list.push(nst)
        # 15 to 29:
        for storm_row in entry_array[15:29]:
            self.log.info(storm_row)
            nst = StormNode(storm_row[0], storm_row[1], storm_row[2], storm_row[3])
            self.linked_list.push_top(nst)
        # Last Item:
        storm_row = entry_array[-1]
        nst = StormNode(storm_row[0], storm_row[1], storm_row[2], storm_row[3])
        self.linked_list.insert(13,nst)
        time_p2 = time.perf_counter_ns()
        time_p2t = time_p2 - time_p1
        # Print forward after chopping up and unsorting list:
        self.linked_list.printForward()
        # Update gui:
        self.log.debug(f"Phase P2: Perf Counter: {time_p2t}")
        header = self.main_window.table_step2.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.render_list_to_qTable(self.linked_list,self.main_window.table_step2)
        self.main_window.time_p2.display(str(time_p2t))
        #
        # Sort the List by Category:
        step2algo = self.main_window.sort1.currentData()
        if (step2algo == "q"):
            self.log.info("QuickSort for Step 3!")
            from .sorters import _partition, linked_quick_sort, _linked_quick_sort
            # OUR Quicksort algorithm executes in place!!!!
            time_p2 = time.perf_counter_ns()
            linked_quick_sort(self.linked_list.head, self.linked_list.tail, 'category')
            time_p3 = time.perf_counter_ns()
            header = self.main_window.table_step3.horizontalHeader()
            header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            self.render_list_to_qTable(self.linked_list, self.main_window.table_step3)
            time_p3t = time_p3 - time_p2
            self.main_window.time_p3.display(str(time_p3t))
        # Print forward after 1st sort:
        print("\n*****\n")
        self.linked_list.printForward()

        # Sort the List by Cost:
        step2algo = self.main_window.sort1.currentData()
        if (step2algo == "q"):
            self.log.info("QuickSort for Step 3!")
            from .sorters import _partition, linked_quick_sort, _linked_quick_sort
            # OUR Quicksort algorithm executes in place!!!!
            time_p3 = time.perf_counter_ns()
            linked_quick_sort(self.linked_list.head, self.linked_list.tail, 'cost')
            time_p4 = time.perf_counter_ns()
            header = self.main_window.table_step4.horizontalHeader()
            header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            self.render_list_to_qTable(self.linked_list, self.main_window.table_step4)
            time_p4t = time_p4 - time_p3
            self.main_window.time_p4.display(str(time_p4t))
            time_tt = time_p4 - time_p0
            self.main_window.statusbar.showMessage(f"Load CSV  and Sort Complete Total time: {time_tt}ns, Loading: {time_p1t}ns., Sort: {time_p2t}ns., Render forwards: {time_p3t}ns., Render backwards:  {time_p4t}ns. Total items: {self.linked_list.count}.")

        # Print forward after 2nd sort:
        print("\n*****\n")
        self.linked_list.printForward()
