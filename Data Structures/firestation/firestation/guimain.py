import logging
import time
import csv
# GUI objects:
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QTableWidgetItem,QMessageBox,QFileDialog


# import our Data struct classes:
from firestation.classes import FireStation,FireStationNode,StationLinkedList


class GUIMain(QObject):
    # Variables we'll need to keep track of:
    # Our linked list:
    linked_list = StationLinkedList()
    log = logging.getLogger(__name__)
    main_window = False
    main_widget = False

    def about(self):
        about_dialog = QMessageBox.information(self.main_widget,"About","Simple FireStation Linked List Demo\nFall 2023  - CCP \n By D. Mann")

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
    def create_card_array(self):
        # Initialize the array to implement Fisher-Yates:
        self.cards = []
        self.shuffled_cards = []
        # Fastest way to iterate through these hashes to create a 2D array is to use two for... statements using the hash indices:
        self.count = 0

        self.log.info("Step 1: Create and populate card Array...")
        # [v] for values, [s] for suits:
        for v in constants.CARD_VALUES:
            for s in constants.CARD_SUITS:
                self.log.info(f"Creating Card {constants.CARD_SUITS[s]}.{constants.CARD_VALUES[v]}...")
                # Create instance of Card and append to array for Fisher-Yates:
                self.cards.append(Card(v, s))
                self.count += 1
        self.log.info(f"Created {self.count} cards.")
        self.print_card_array(self.cards)


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
            # Station #:
            table_widget.setItem(i, 0, QTableWidgetItem(str(item.station.number)))
            # Station Location:
            table_widget.setItem(i, 1, QTableWidgetItem(item.station.location))
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
            # Station #:
            table_widget.setItem(i, 0, QTableWidgetItem(str(item.station.number)))
            # Station Location:
            table_widget.setItem(i, 1, QTableWidgetItem(item.station.location))
            # Increment counter:
            i += 1
            item = item.get_prev()



    def parse_csv(self,file):
        csvreader = csv.reader(file)
        # skip header:
        csvreader.__next__()
        # Step through the rows and load the linked list:
        for station_row in csvreader:
            # Create a Storm Linked list and Node instance for each row:
            self.log.info(f"Creating a new node for Station {station_row}")
            nst = FireStationNode(int(station_row[0]), station_row[1])
            self.linked_list.push(nst)

    def list_all_steps(self):
        # Step 1: Select file:
        csv_file = self.open_file_name_dialog()
        # Now open and parse it:
        time_p0 = time.perf_counter_ns()
        self.log.debug(f"Source File: {csv_file}")
        with open(csv_file,"r") as open_file:
            self.parse_csv(open_file)
            open_file.close()
        time_p1 = time.perf_counter_ns()
        # And it's perf counter:
        time_p1t = time_p1 - time_p0
        # Update gui:
        self.log.debug(f"Phase P1: Perf Counter: {time_p1t}")
        self.render_list_to_qTable(self.linked_list,self.main_window.table_step1)
        self.main_window.time_p1.display(str(time_p1t))

        # Step 2: Execute Sort:
        self.log.info("Step 2: Execute Sort")
        time_p1 = time.perf_counter_ns()
        step2algo = self.main_window.sort1.currentData()
        time_p2 = time.perf_counter_ns()
        if (step2algo == "q"):
            time_p2 = time.perf_counter_ns()
            self.log.info("QuickSort for Step 2!")
            from .sorters import _partition, linked_quick_sort, _linked_quick_sort
            # OUR Quicksort algorithm executes in place!!!!
            linked_quick_sort(self.linked_list.head, self.linked_list.tail, 'number')

        time_p2t = time_p2 - time_p1
        # Update gui:
        self.log.debug(f"Phase P2: Perf Counter: {time_p2t}")
        self.render_list_to_qTable(self.linked_list,self.main_window.table_step2)
        self.main_window.time_p2.display(str(time_p2t))

        # Now just draw the list twice to the gui, forwards and backwards:
        time_p2 = time.perf_counter_ns()
        self.render_list_to_qTable(self.linked_list, self.main_window.table_step3)
        time_p3 = time.perf_counter_ns()
        time_p3t = time_p3 - time_p2
        self.main_window.time_p3.display(str(time_p3t))

        # And finally, backwards:
        time_p3 = time.perf_counter_ns()
        self.render_list_to_qTable_backwards(self.linked_list, self.main_window.table_step4)
        time_p4 = time.perf_counter_ns()
        time_p4t = time_p4 - time_p3
        self.main_window.time_p4.display(str(time_p4t))
        time_tt = time_p4 - time_p0

        self.main_window.statusbar.showMessage(f"Load CSV  and Sort Complete Total time: {time_tt}ns, Loading: {time_p1t}ns., Sort: {time_p2t}ns., Render forwards: {time_p3t}ns., Render backwards:  {time_p4t}ns. Total items: {self.linked_list.count}.")





