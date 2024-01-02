import logging
import time

# GUI objects:
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QTableWidgetItem,QMessageBox

# Suits and Values:
from cardShuffle import constants
# import our Card class:
from cardShuffle.card import Card
# And Fisher-Yates:
from cardShuffle.fisherYates import shuffle
# Sorters:
from cardShuffle import sorters
class GUIMain(QObject):
    # Variables we'll need to keep track of:
    cards = []
    shuffled_cards = []
    count = 0
    log = logging.getLogger(__name__)
    main_window = False
    main_widget = False

    def about(self):
        about_dialog = QMessageBox.information(self.main_widget,"About","Simple Card Shuffle and Sort Demo\nFall 2023  - CCP \n By D. Mann")

    def dontclickme(self):
        dcm_dialog = QMessageBox.critical(self.main_widget,"ABSOLUTE MADNESS!!","I told you to not click that button!!!!!")
        dcm_dialog = QMessageBox.critical(self.main_widget,"ABSOLUTE MADNESS!!","I really would have rather you NOT clicked that!!!!")
        dcm_dialog = QMessageBox.critical(self.main_widget,"ABSOLUTE MADNESS!!","Now you're suffering the consequences of your actions!!!!!")
        dcm_dialog = QMessageBox.critical(self.main_widget,"ABSOLUTE MADNESS!!","Don't click it again!!!!!!")
    def print_card_array(self,array):
        for item in array:
            print(f"{constants.CARD_VALUES[item.value]} - {constants.CARD_SUITS[item.suit]}")

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
        for k,v in [("i","Insert Sort"),
                    ("s","Selection Sort"),
                    # ("c","Count Sort"),
                    ("m","Merge Sort"),
                    ("q","Quicksort")]:
            self.main_window.sort1.addItem(v,k)
            self.main_window.sort2.addItem(v,k)



    def render_cards_to_qTable(self,cards,table_widget):
        # first, empty out the table:
        table_widget.setRowCount(0)
        # Now, insert every row:
        i = 0
        for item in cards:
            # Create row:
            table_widget.insertRow(i)
            # Populate Row:
            # suit:
            table_widget.setItem(i, 0, QTableWidgetItem(constants.CARD_SUITS[item.suit]))
            # value:
            table_widget.setItem(i, 1, QTableWidgetItem(constants.CARD_VALUES[item.value]))
            # Increment counter:
            i += 1






    def shuffle_all_steps(self):
        # Step 1: Create Card Array:
        # Performance counters:
        time_p0 = time.perf_counter_ns()
        self.create_card_array()
        time_p1 = time.perf_counter_ns()
        # Now populate the contents of the first Table:
        self.render_cards_to_qTable(self.cards,self.main_window.table_source)
        # And it's perf counter:
        time_p1t = time_p1 - time_p0
        self.log.debug(f"Phase P1: Perf Counter: {time_p1t}")
        self.main_window.time_p1.display(str(time_p1t))

        # Now, do Fisher-Yates  randomisation:

        self.log.info("Step 2: Shuffle it with Fisher-Yates...")
        # Shuffle and proof:
        time_p1 = time.perf_counter_ns()
        self.shuffled_cards = shuffle(self.cards)
        time_p2 = time.perf_counter_ns()
        self.render_cards_to_qTable(self.shuffled_cards,self.main_window.table_fisher)
        # And it's perf counter:
        time_p2t = time_p2 - time_p1
        self.log.debug(f"Phase P2: Perf Counter: {time_p2t}")
        self.main_window.time_p2.display(str(time_p2t))

        # Now do Step 3 Sorting, based on user selections:
        step3algo = self.main_window.sort1.currentData()
        # Insertion Sort mode:
        if (step3algo == "i"):
            time_p2 = time.perf_counter_ns()
            self.log.info("Insertion Sort for Step 3!")
            sorted_first = sorters.insertionSort(self.shuffled_cards,"value")
            time_p3 = time.perf_counter_ns()
        # Selection Sort Mode:
        elif (step3algo == "s"):
            time_p2 = time.perf_counter_ns()
            self.log.info("Selection Sort for Step 3!")
            sorted_first = sorters.selectionSort(self.shuffled_cards, "value")
            time_p3 = time.perf_counter_ns()
        # count Sort mode:
        elif (step3algo == "c"):
            time_p2 = time.perf_counter_ns()
            self.log.info("Count Sort for Step 3!")
            sorted_first = sorters.countSort(self.shuffled_cards, "value")
            time_p3 = time.perf_counter_ns()
        # Merge sort mode:
        elif (step3algo == "m"):
            time_p2 = time.perf_counter_ns()
            self.log.info("Merge Sort for Step 3!")
            sorted_first = sorters.mergeSort(self.shuffled_cards, "value")
            time_p3 = time.perf_counter_ns()
        # Quick sort mode:
        elif (step3algo == "q"):
            time_p2 = time.perf_counter_ns()
            self.log.info("QuickSort for Step 3!")
            sorted_first = sorters.quickSort(self.shuffled_cards, "value",0,self.count-1)
            time_p3 = time.perf_counter_ns()


        time_p3t = time_p3-time_p2

        self.log.debug(f"Phase P3: Perf Counter: {time_p3t}")
        self.render_cards_to_qTable(sorted_first, self.main_window.table_sort1)
        self.main_window.time_p3.display(str(time_p3t))



        # Step 4 - as above:
        step4algo = self.main_window.sort2.currentData()
        # Insertion Sort mode:
        if (step4algo == "i"):
            time_p3 = time.perf_counter_ns()
            self.log.info("Insertion Sort for Step 4!")
            sorted_first = sorters.insertionSort(sorted_first, "suit")
            time_p4 = time.perf_counter_ns()
        # Selection Sort Mode:
        elif (step4algo == "s"):
            time_p3 = time.perf_counter_ns()
            self.log.info("Selection Sort for Step 4!")
            sorted_first = sorters.selectionSort(sorted_first, "suit")
            time_p4 = time.perf_counter_ns()
        # Merge Sort Mode:
        elif (step4algo == "m"):
            #self.print_card_array(sorted_first)
            time_p3 = time.perf_counter_ns()
            self.log.info("Merge Sort for Step 4!")
            # For a second Merge sort; make sure the array is entered in the right order before sorting is implemented:
            sorted_first = sorters.mergeSort(sorted_first[::-1], "suit")
            time_p4 = time.perf_counter_ns()
            #self.print_card_array(sorted_first)
        # Quick sort mode:
        # elif (step4algo == "q"):
        #     time_p3 = time.perf_counter_ns()
        #     self.log.info("QuickSort for Step 4!")
        #     sorted_first = sorters.quickSort(sorted_first, "suit",0,self.count-1)
        #     time_p4 = time.perf_counter_ns()

        time_p4t = time_p4 - time_p3
        self.log.debug(f"Phase P3: Perf Counter: {time_p4t}")
        self.render_cards_to_qTable(sorted_first, self.main_window.table_sort2)
        self.main_window.time_p4.display(str(time_p4t))
        time_tt = time_p4 - time_p0
        sort_1_name = self.main_window.sort1.itemText(self.main_window.sort1.currentIndex())
        sort_2_name = self.main_window.sort2.itemText(self.main_window.sort2.currentIndex())
        self.main_window.statusbar.showMessage(f"Shuffle and Sort Complete Total time: {time_tt}ns, Creation: {time_p1t}ns., Randomiser: {time_p2t}ns., {sort_1_name}: {time_p3t}ns., {sort_2_name}: {time_p4t}ns.")





