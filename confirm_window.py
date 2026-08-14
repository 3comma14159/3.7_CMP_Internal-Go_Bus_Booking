from tkinter import *
from tkinter import ttk
import re

class Confirm:
    def __init__(self, parent):
        f = open("go_bus_booking.txt", "w+")
        f.truncate(0)
        f.seek(0)
        f.write("Every line is one booking. The information is written the following way: Name, number, PNA seats amount, PNA beds amount, APN seats amoung, APN beds amount, total price, gst portion\n")
        f.close()

        # creating colour variables
        white = "#FFFFFF"
        grey = "#E6E6E6"
        blue = "#004B8D"
        gold = "#E4A024"
        red = "#FFCCCC"
        purple = "#9933FF"
        green = "#00CC00"

        self.name = "First Name Last Name"
        self.number = "+64 21 012 345"
        self.PNA_seats_amount = 3
        self.PNA_beds_amount = 0
        self.APN_seats_amount = 2
        self.APN_beds_amount = 1
        self.PNA_seats_price = self.PNA_seats_amount*25
        self.PNA_beds_price = self.PNA_beds_amount*50
        self.APN_seats_price = self.APN_seats_amount*25
        self.APN_beds_price = self.APN_beds_amount*50
        self.total = self.PNA_seats_price + self.PNA_beds_price + self.APN_seats_price + self.APN_beds_price
        self.gst_portion = round((self.total - (self.total/1.15)), 2)

        # confirm frame
        self.confirm_frame = Frame(bg=gold, pady=10)
        self.confirm_frame.grid()

        # heading (row 0)
        self.heading_label = Label(self.confirm_frame, text="Your Booking", font="Helvetica 20 bold", bg=gold, fg=white, padx=10, pady=10)
        self.heading_label.grid(row=0)

        # instructions (row 1)
        self.instructions_label = Label(self.confirm_frame, text="Please check your name, number and booking.", font="Helvetica 12 italic", bg=gold, fg=white, pady=10, padx=10)
        self.instructions_label.grid(row=1)

        # name (row 2)
        self.name_label = Label(self.confirm_frame, bg=blue, fg=white, text=f"Name: {self.name}", font="Helvetica 14", anchor="w", highlightthickness=2, highlightbackground=white, relief="flat", padx=12, pady=5)
        self.name_label.grid(row=2, padx=20, pady=5, sticky="ew")

        # number (row 3)
        self.number_label = Label(self.confirm_frame, bg=blue, fg=white, text=f"Number: {self.number}", font="Helvetica 14", anchor="w", highlightthickness=2, highlightbackground=white, relief="flat", padx=12, pady=5)
        self.number_label.grid(row=3, padx=20, pady=5, sticky="ew")


        # -------------------------------------------------------------------------------------------------------
        #                                   PN -> A table
        # -------------------------------------------------------------------------------------------------------

        # PNA frame (row 4)
        self.PNA_frame = Frame(self.confirm_frame, bg=blue, highlightthickness=2, highlightbackground=white)
        self.PNA_frame.grid(row=4, padx=20, pady=(15, 10), columnspan=7, sticky="ew")

        # PNA header -------------------------------------------------------------------------------------------------------
        
        # PNA heading (row 0)
        self.PNA_heading_label = Label(self.PNA_frame, bg=blue, fg=white, text="Palmerston North -> Auckland", font="Helvetica 12 bold", justify=CENTER, padx=10)
        self.PNA_heading_label.grid(row=0, pady=(5, 7), columnspan=7, sticky="ew")


        # line separation (row 1)
        self.PNA_separator = Frame(self.PNA_frame, bg=white, height=2)
        self.PNA_separator.grid(row=1, columnspan=7, sticky="ew")

        # PNA categories -------------------------------------------------------------------------------------------------------
        
        # PNA category frame (row 2)
        self.PNA_category_frame = Frame(self.PNA_frame, bg=blue)
        self.PNA_category_frame.grid(row=2, columnspan=7, sticky="ew")

        # PNA seats heading (row 0, col 0 &1&2)
        self.PNA_seats_heading_label = Label(self.PNA_category_frame, bg=blue, fg=white, text="Seats", font="Helvetica 12 bold", justify=CENTER, padx=8, pady=5)
        self.PNA_seats_heading_label.grid(row=0, column=0, columnspan=3, sticky="ew")

        # PNA column category separation (row 0, col 3)
        self.PNA_category_separator = Frame(self.PNA_category_frame, bg=white, width=2)
        self.PNA_category_separator.grid(row=0, column=3, columnspan=1, sticky="ns")

        # PNA beds heading (row 0, col 4)
        self.PNA_beds_heading_label = Label(self.PNA_category_frame, bg=blue, fg=white, text="Beds", font="Helvetica 12 bold", justify=CENTER, padx=10, pady=5)
        self.PNA_beds_heading_label.grid(row=0, column=4, columnspan=3, sticky="ew")


        # line separation (row 3)
        self.PNA_separator = Frame(self.PNA_frame, bg=white, height=2)
        self.PNA_separator.grid(row=3, columnspan=7, sticky="ew")

        # PNA values -------------------------------------------------------------------------------------------------------
        
        # PNA values frame (row 4)
        self.PNA_values_frame = Frame(self.PNA_frame, bg=blue)
        self.PNA_values_frame.grid(row=4, columnspan=7, sticky="ew")

        # PNA seats amount (row 0 col 0)
        self.PNA_seats_number_label = Label(self.PNA_values_frame, bg=blue, fg=white, text=self.PNA_seats_amount, font="Helvetica 12", justify= CENTER, padx=10, pady=5)
        self.PNA_seats_number_label.grid(row=0, column=0, columnspan=1, sticky="ew")

        # PNA column seats separator (row 0 col 1)
        self.PNA_seats_separator = Frame(self.PNA_values_frame, bg=white, width=2)
        self.PNA_seats_separator.grid(row=0, column=1, columnspan=1, sticky="ns")

        # PNA seats price (row 0 col 2)
        self.PNA_seats_price_label = Label(self.PNA_values_frame, bg=blue, fg=white, text=f"${self.PNA_seats_price}", font="Helvetica 12", justify= CENTER, padx=10, pady=5)
        self.PNA_seats_price_label.grid(row=0, column=2, columnspan=1, sticky="ew")

        # PNA column seats beds separator (row 0 col 3)
        self.PNA_seats_beds_separator = Frame(self.PNA_values_frame, bg=white, width=2)
        self.PNA_seats_beds_separator.grid(row=0, column=3, columnspan=1, sticky="ns")

        # PNA beds amount (row 0 col 4)
        self.PNA_beds_number_label = Label(self.PNA_values_frame, bg=blue, fg=white, text=self.PNA_beds_amount, font="Helvetica 12", justify= CENTER, padx=10, pady=5)
        self.PNA_beds_number_label.grid(row=0, column=4, columnspan=1, sticky="ew")

        # PNA column beds separator (row 0 col 5)
        self.PNA_beds_separator = Frame(self.PNA_values_frame, bg=white, width=2)
        self.PNA_beds_separator.grid(row=0, column=5, columnspan=1, sticky="ns")

        # PNA beds price (row 0 col 6)
        self.PNA_beds_price_label = Label(self.PNA_values_frame, bg=blue, fg=white, text=f"${self.PNA_beds_price}", font="Helvetica 12", justify= CENTER, padx=10, pady=5)
        self.PNA_beds_price_label.grid(row=0, column=6, columnspan=1, sticky="ew")

        # -------------------------------------------------------------------------------------------------------
        # specifying column widths
        for column in range(7):
            self.PNA_frame.columnconfigure(column, weight=1)

        for column in [0, 1, 2, 4, 5, 6]:
            self.PNA_category_frame.columnconfigure(column, weight=1, uniform="category")
        self.PNA_category_frame.columnconfigure(3, weight=0, minsize=2)

        for column in [0, 2, 4, 6]:
            self.PNA_values_frame.columnconfigure(column, weight=1, uniform="values")
        for column in [1, 3, 5]:
            self.PNA_values_frame.columnconfigure(column, weight=0, minsize=2)

        # -------------------------------------------------------------------------------------------------------
        #                                   A -> PN table
        # -------------------------------------------------------------------------------------------------------

        # APN frame (row 5)
        self.APN_frame = Frame(self.confirm_frame, bg=blue, highlightthickness=2, highlightbackground=white)
        self.APN_frame.grid(row=5, padx=20, pady=10, columnspan=7, sticky="ew")

        # APN header -------------------------------------------------------------------------------------------------------
        
        # APN heading (row 0)
        self.APN_heading_label = Label(self.APN_frame, bg=blue, fg=white, text="Auckland -> Palmerston North", font="Helvetica 12 bold", justify=CENTER, padx=10)
        self.APN_heading_label.grid(row=0, pady=(5, 7), columnspan=7, sticky="ew")


        # line separation (row 1)
        self.APN_separator = Frame(self.APN_frame, bg=white, height=2)
        self.APN_separator.grid(row=1, columnspan=7, sticky="ew")

        # APN categories -------------------------------------------------------------------------------------------------------
        
        # APN category frame (row 2)
        self.APN_category_frame = Frame(self.APN_frame, bg=blue)
        self.APN_category_frame.grid(row=2, columnspan=7, sticky="ew")

        # APN seats heading (row 0, col 0 &1&2)
        self.APN_seats_heading_label = Label(self.APN_category_frame, bg=blue, fg=white, text="Seats", font="Helvetice 12 bold", justify=CENTER, padx=8, pady=5)
        self.APN_seats_heading_label.grid(row=0, column=0, columnspan=3, sticky="ew")

        # APN column category separation (row 0, col 3)
        self.APN_category_separator = Frame(self.APN_category_frame, bg=white, width=2)
        self.APN_category_separator.grid(row=0, column=3, columnspan=1, sticky="ns")

        # APN beds heading (row 0, col 4)
        self.APN_beds_heading_label = Label(self.APN_category_frame, bg=blue, fg=white, text="Beds", font="Helvetice 12 bold", justify=CENTER, padx=10, pady=5)
        self.APN_beds_heading_label.grid(row=0, column=4, columnspan=3, sticky="ew")


        # line separation (row 3)
        self.APN_separator = Frame(self.APN_frame, bg=white, height=2)
        self.APN_separator.grid(row=3, columnspan=7, sticky="ew")

        # APN values-------------------------------------------------------------------------------------------------------
        
        # APN values frame (row 4)
        self.APN_values_frame = Frame(self.APN_frame, bg=blue)
        self.APN_values_frame.grid(row=4, columnspan=7, sticky="ew")

        # APN seats amount (row 0 col 0)
        self.APN_seats_number_label = Label(self.APN_values_frame, bg=blue, fg=white, text=self.APN_seats_amount, font="Helvetica 12", justify= CENTER, padx=10, pady=5)
        self.APN_seats_number_label.grid(row=0, column=0, columnspan=1, sticky="ew")

        # APN column seats separator (row 0 col 1)
        self.APN_seats_separator = Frame(self.APN_values_frame, bg=white, width=2)
        self.APN_seats_separator.grid(row=0, column=1, columnspan=1, sticky="ns")

        # APN seats price (row 0 col 2)
        self.APN_seats_price_label = Label(self.APN_values_frame, bg=blue, fg=white, text=f"${self.APN_seats_price}", font="Helvetica 12", justify= CENTER, padx=10, pady=5)
        self.APN_seats_price_label.grid(row=0, column=2, columnspan=1, sticky="ew")

        # APN column seats beds separator (row 0 col 3)
        self.APN_seats_beds_separator = Frame(self.APN_values_frame, bg=white, width=2)
        self.APN_seats_beds_separator.grid(row=0, column=3, columnspan=1, sticky="ns")

        # APN beds amount (row 0 col 4)
        self.APN_beds_number_label = Label(self.APN_values_frame, bg=blue, fg=white, text=self.APN_beds_amount, font="Helvetica 12", justify= CENTER, padx=10, pady=5)
        self.APN_beds_number_label.grid(row=0, column=4, columnspan=1, sticky="ew")

        # APN column beds separator (row 0 col 5)
        self.APN_beds_separator = Frame(self.APN_values_frame, bg=white, width=2)
        self.APN_beds_separator.grid(row=0, column=5, columnspan=1, sticky="ns")

        # APN beds price (row 0 col 6)
        self.APN_beds_price_label = Label(self.APN_values_frame, bg=blue, fg=white, text=f"${self.APN_beds_price}", font="Helvetica 12", justify= CENTER, padx=10, pady=5)
        self.APN_beds_price_label.grid(row=0, column=6, columnspan=1, sticky="ew")

        # -------------------------------------------------------------------------------------------------------
        # specifying column widths
        for column in range(7):
            self.APN_frame.columnconfigure(column, weight=1)
        
        for column in [0, 1, 2, 4, 5, 6]:
            self.APN_category_frame.columnconfigure(column, weight=1, uniform="category")
        self.APN_category_frame.columnconfigure(3, weight=0, minsize=2)
        
        for column in [0, 2, 4, 6]:
            self.APN_values_frame.columnconfigure(column, weight=1, uniform="values")
        for column in [1, 3, 5]:
            self.APN_values_frame.columnconfigure(column, weight=0, minsize=2)
        # -------------------------------------------------------------------------------------------------------
        #                                   Total, GST, Edit & Save Buttons
        # -------------------------------------------------------------------------------------------------------

        # total, gst frame (row 6)
        self.total_gst_frame = Frame(self.confirm_frame, bg=blue, highlightthickness=2, highlightbackground=white)
        self.total_gst_frame.grid(row=6, padx=20, pady=10, sticky="ew")

        # total (row 0, col 0)
        self.total_label = Label(self.total_gst_frame, bg=blue, fg=white, text=f"Total: ${self.total}", font="Helvetice 12 bold", justify=CENTER, padx=8, pady=5)
        self.total_label.grid(row=0, column=0, sticky="ew")

        # separator (row 0, col 1)
        self.total_gst_separator = Frame(self.total_gst_frame, bg=white, width=2)
        self.total_gst_separator.grid(row=0, column=1, sticky="ns")

        # gst (row 0, col 2)
        self.gst_label = Label(self.total_gst_frame, bg=blue, fg=white, text=f"GST Portion: ${self.gst_portion}", font="Helvetice 12 bold", justify=CENTER, padx=10, pady=5)
        self.gst_label.grid(row=0, column=2, sticky="ew")

        self.total_gst_frame.columnconfigure(1, weight=0, minsize=2)

        # Buttons -------------------------------------------------------------------------------------------------------

        # edit, save buttons frame (row 7)
        self.edit_save_frame = Frame(self.confirm_frame, bg=blue, highlightthickness=2, highlightbackground=white)
        self.edit_save_frame.grid(row=7, padx=20, pady=10, sticky="ew")

        self.style = ttk.Style()
        self.style.theme_use('clam')

        # edit button style
        self.style.configure('Edit.TButton', background=purple, focuscolor=purple, foreground=white, font="Helvetica 16 bold", padding=(10, 5), borderwidth=0) #focus color
        self.style.map('Edit.TButton', background=[('active', purple), ('pressed', purple)], foreground=[('active', white), ('pressed', white)], focuscolor=[('active', purple), ('pressed', purple)])

        # edit button style
        self.style.configure('Save.TButton', background=green, focuscolor=green, foreground=white, font="Helvetica 16 bold", padding=(10, 5), borderwidth=0) #focus color
        self.style.map('Save.TButton', background=[('active', green), ('pressed', green)], foreground=[('active', white), ('pressed', white)], focuscolor=[('active', green), ('pressed', green)])

        # edit button (row 0, col 0)
        self.edit_button = ttk.Button(self.edit_save_frame, text="Edit", style="Edit.TButton", command=self.edit)
        self.edit_button.grid(row=0, column=0, sticky="ew")

        # separator (row 0, col 1)
        self.edit_save_separator = Frame(self.edit_save_frame, bg=white, width=2)
        self.edit_save_separator.grid(row=0, column=1, sticky="ns")

        # save button (row 0, col 2)
        self.save_button = ttk.Button(self.edit_save_frame, text="Save", style="Save.TButton", command=self.save)
        self.save_button.grid(row=0, column=2, sticky="ew")

        self.edit_save_separator.columnconfigure(1, weight=0, minsize=2)

    def edit(self):
        print("Edit")
        self.confirm_frame.destroy()

    def save(self):
        name = self.name
        number = self.number
        PNA_seats_amount = self.PNA_seats_amount
        PNA_beds_amount = self.PNA_beds_amount
        APN_seats_amount = self.APN_seats_amount
        APN_beds_amount = self.APN_beds_amount
        total = self.total
        gst = self.gst_portion

        text = f"{name}, {number}, {PNA_seats_amount}, {PNA_beds_amount}, {APN_seats_amount}, {APN_beds_amount}, {total}, {gst}"

        f = open("go_bus_booking.txt", "a")
        f.write(text + "\n")
        f.close()

        print("save")
        
        self.confirm_frame.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.configure()
    root.title("Go Bus Booking")
    something = Confirm(root)
    root.mainloop()