from tkinter import *
from tkinter import ttk
import re

class Confirm:
    def __init__(self, parent):
        # creating colour variables
        white = "#FFFFFF"
        grey = "#E6E6E6"
        blue = "#004B8D"
        gold = "#E4A024"
        red = "#FFCCCC"
        purple = "#9933FF"
        green = "#00CC00"

        name = "First Name Last Name"
        number = "+64 21 012 345"
        PNA_seats_amount = 3
        PNA_beds_amount = 0
        APN_seats_amount = 2
        APN_beds_amount = 1
        PNA_seats_price = PNA_seats_amount*25
        PNA_beds_price = PNA_beds_amount*50
        APN_seats_price = APN_seats_amount*25
        APN_beds_price = APN_beds_amount*50

        # confirm frame
        self.confirm_frame = Frame(bg=gold, pady=10)
        self.confirm_frame.grid()

        # PN -> A

        # PNA frame (row 0)
        self.PNA_frame = Frame(self.confirm_frame, bg=blue, highlightthickness=2, highlightbackground=white)
        self.PNA_frame.grid(row=0, padx=20, pady=20, columnspan=1, sticky="ew")

        # PNA heading (row 0)
        self.PNA_heading_label = Label(self.PNA_frame, bg=blue, fg=white, text="Palmerston North -> Auckland", font="Helvetica 12 bold", justify=CENTER, padx=10)
        self.PNA_heading_label.grid(row=0, pady=(5, 7), columnspan=1, sticky="ew")

        # line separation (row 1)
        self.PNA_separator = Frame(self.PNA_frame, bg=white, height=2)
        self.PNA_separator.grid(row=1, columnspan=7, sticky="ew")

        # PNA category frame (row 2)
        self.PNA_category_frame = Frame(self.PNA_frame, bg=blue)
        self.PNA_category_frame.grid(row=2, columnspan=3, sticky="ew")

        # PNA seats heading (row 0, col 0 &1&2)
        self.PNA_seats_heading_label = Label(self.PNA_category_frame, bg=blue, fg=white, text="Seats", font="Helvetice 12 bold", justify=CENTER, padx=10, pady=5)
        self.PNA_seats_heading_label.grid(row=0, column=0, columnspan=1, sticky="ew")

        # PNA column category separation (row 0, col 3)
        self.PNA_category_separator = Frame(self.PNA_category_frame, bg=white, width=2)
        self.PNA_category_separator.grid(row=0, column=1, columnspan=1, sticky="ns")

        # PNA beds heading (row 0, col 4)
        self.PNA_beds_heading_label = Label(self.PNA_category_frame, bg=blue, fg=white, text="Beds", font="Helvetice 12 bold", justify=CENTER, padx=10, pady=5)
        self.PNA_beds_heading_label.grid(row=0, column=2, columnspan=1, sticky="ew")

        # line separation (row 3)
        self.PNA_separator = Frame(self.PNA_frame, bg=white, height=2)
        self.PNA_separator.grid(row=3, columnspan=1, sticky="ew")

        # PNA values frame (row 4)
        self.PNA_values_frame = Frame(self.PNA_frame, bg=blue)
        self.PNA_values_frame.grid(row=4, columnspan=7, sticky="ew")

        # PNA seats amount (row 0 col 0)
        self.PNA_seats_number_label = Label(self.PNA_values_frame, bg=blue, fg=white, text=PNA_seats_amount, font="Helvetica 12", justify= CENTER, padx=10, pady=5)
        self.PNA_seats_number_label.grid(row=0, column=0, columnspan=1, sticky="ew")

        # PNA column seats separator (row 0 col 1)
        self.PNA_seats_separator = Frame(self.PNA_values_frame, bg=white, width=2)
        self.PNA_seats_separator.grid(row=0, column=1, columnspan=1, sticky="ns")

        # PNA seats price (row 0 col 2)
        self.PNA_seats_price_label = Label(self.PNA_values_frame, bg=blue, fg=white, text=f"${PNA_seats_price}", font="Helvetica 12", justify= CENTER, padx=10, pady=5)
        self.PNA_seats_price_label.grid(row=0, column=2, columnspan=1, sticky="ew")

        # PNA column seats beds separator (row 0 col 3)
        self.PNA_seats_beds_separator = Frame(self.PNA_values_frame, bg=white, width=2)
        self.PNA_seats_beds_separator.grid(row=0, column=3, columnspan=1, sticky="ns")

        # PNA beds amount (row 0 col 4)
        self.PNA_beds_number_label = Label(self.PNA_values_frame, bg=blue, fg=white, text=PNA_beds_amount, font="Helvetica 12", justify= CENTER, padx=10, pady=5)
        self.PNA_beds_number_label.grid(row=0, column=4, columnspan=1, sticky="ew")

        # PNA column beds separator (row 0 col 5)
        self.PNA_beds_separator = Frame(self.PNA_values_frame, bg=white, width=2)
        self.PNA_beds_separator.grid(row=0, column=5, columnspan=1, sticky="ns")

        # PNA beds price (row 0 col 6)
        self.PNA_beds_price_label = Label(self.PNA_values_frame, bg=blue, fg=white, text=f"${PNA_beds_price}", font="Helvetica 12", justify= CENTER, padx=10, pady=5)
        self.PNA_beds_price_label.grid(row=0, column=6, columnspan=1, sticky="ew")

        # specifying column widths
        self.PNA_category_frame.columnconfigure(0, weight=1, uniform="category")
        self.PNA_category_frame.columnconfigure(2, weight=1, uniform="category")
        self.PNA_category_frame.columnconfigure(1, weight=0, minsize=2)

        for column in [0, 2, 4, 6]:
            self.PNA_values_frame.columnconfigure(column, weight=1, uniform="values")
        for column in [1, 3, 5]:
            self.PNA_values_frame.columnconfigure(column, weight=0, minsize=2)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.configure()
    root.title("Go Bus Booking")
    something = Confirm(root)
    root.mainloop()