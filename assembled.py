from tkinter import *
from tkinter import ttk
import re

class Booking:
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

        self.PNA_available_seats = 20
        self.PNA_available_beds = 15
        self.APN_available_seats = 20
        self.APN_available_beds = 15

        self.style = ttk.Style()
        self.style.theme_use('clam')

        # spinbox style
        self.style.configure('amount.TSpinbox', fieldbackground=gold, background=gold, arrowcolor=blue, foreground=white, bordercolor=gold, lightcolor=gold, darkcolor=gold)
        self.style.map('amount.TSpinbox', bordercolor=[('focus', gold)], lightcolor=[('focus', gold)], darkcolor=[('focus', gold)], fieldbackground=[('focus', gold)], foreground=[('focus', white)], selectbackground=[('focus', gold), ('!focus', gold)], selectforeground=[('focus', white), ('!focus', white)])

        # book button style
        self.style.configure('Book.TButton', background=gold, foreground=white, font="Helvetica 16 bold", padding=(10, 5), borderwidth=4, bordercolor=gold, lightcolor=gold, darkcolor=gold, focuscolor=gold)
        self.style.map('Book.TButton', background=[('active', gold), ('pressed', gold)], foreground=[('active', white), ('pressed', white)], bordercolor=[('active', white), ('pressed', white)], lightcolor=[('active', white), ('pressed', white)], darkcolor=[('active', white), ('pressed', white)], focuscolor=[('active', gold), ('pressed', gold)])

        # placeholder function to give instructions for name and phone number entry fields
        def placeholder_setup(entry, placeholder):
            # placholder text displayed in grey
            entry.insert(0, placeholder)
            entry.config(fg=grey)

            # when nothing has been entered yet, placeholder is removed
            def clear_placeholder(event):
                if event.widget.get() == placeholder:
                    event.widget.delete(0, "end")
                    event.widget.config(fg=white)

            # when nothing has been entered and field is not clicked, placeholder text is added
            def add_placeholder(event):
                if len(event.widget.get()) == 0:
                    event.widget.insert(0, placeholder)
                    event.widget.config(fg=grey)

            # when field clicked or left, placeholder clear and add functions are called
            entry.bind("<FocusIn>", clear_placeholder)
            entry.bind("<FocusOut>", add_placeholder)

        # validation function to check if spin box input is numeric and within amount of available seats/beds or empty
        def validate_spinbox(new_value, limit):
            if (new_value.isdigit() and int(new_value)<=limit) or new_value == "":
                return True
            return False

        # empty spinbox -> 0 inserted
        def spin_box_focus_out(event):
            if event.widget.get() == "":
                event.widget.delete(0, "end")
                event.widget.insert(0, "0")
        
        # booking frame
        self.booking_frame = Frame(parent, bg=blue, pady=10)
        self.booking_frame.grid()

        # heading (row 0)
        self.heading_label = Label(self.booking_frame, text="Go Bus Booking", font="Helvetica 20 bold", bg=blue, fg=white, padx=10, pady=10)
        self.heading_label.grid(row=0)

        # instructions (row 1)
        self.instructions_label = Label(self.booking_frame, text="Please enter your full name, phone number\nand the amount of tickets you want to buy.\nThe following prices include GST:\nA seat costs $25 and a bed costs $50.", font="Helvetica 12 italic", bg=blue, fg=white, pady=10, padx=10)
        self.instructions_label.grid(row=1)

        # name input (row 2) - put entry box in a frame to have more style options
        self.name_frame = Frame(self.booking_frame, bg=gold, borderwidth=0, highlightthickness=2, highlightbackground=white)
        self.name_frame.grid(row=2, padx=20, pady=5)
        
        self.name_entry = Entry(self.name_frame, font="Helvetica 14", bg=gold, fg=white, highlightthickness=0, bd=0)
        self.name_entry.grid(padx=12, pady=5)
        placeholder_setup(self.name_entry, "Enter your full name")

        # phone number input (row 3) - put entry box in a frame to have more style options
        self.number_frame = Frame(self.booking_frame, bg=gold, borderwidth=0, highlightthickness=2, highlightbackground=white)
        self.number_frame.grid(row=3, padx=20, pady=5)
                
        self.number_entry = Entry(self.number_frame, font="Helvetica 14", bg=gold, fg=white, highlightthickness=0, bd=0)
        self.number_entry.grid(padx=12, pady=5)
        placeholder_setup(self.number_entry, "Enter your phone number")



        # PN -> A
        # frame (row 4)
        self.PNA_frame = Frame(self.booking_frame, bg=gold, highlightthickness=2, highlightbackground=white)
        self.PNA_frame.grid(row=4, pady=(20, 10))

        # PNA heading (row 0)
        self.PNA_heading_label = Label(self.PNA_frame, text="Palmerston North -> Auckland", font="Helvetica 12 bold", justify=CENTER, bg=gold, fg=white, padx=10)
        self.PNA_heading_label.grid(row=0, pady=(5, 7))

        # line seperation (row 1)
        self.PNA_separator = Frame(self.PNA_frame, bg=white, height=2)
        self.PNA_separator.grid(row=1, sticky="ew")

        # PN -> A spinbox & availability for seats
        # frame (row 2)
        self.PNA_seats_frame = Frame(self.PNA_frame, background=gold, borderwidth=0)
        self.PNA_seats_frame.grid(row=2, pady=(7, 7))

        # spinbox (row 0, column 0)
        validate_PNA_seats = parent.register(lambda P: validate_spinbox(P, self.PNA_available_seats))
        self.PNA_seats_spinbox = ttk.Spinbox(self.PNA_seats_frame, width=2, style='amount.TSpinbox', justify=RIGHT, font="Helvetica 12", from_=0, to=self.PNA_available_seats, validate="key", validatecommand=(validate_PNA_seats, '%P'))
        self.PNA_seats_spinbox.grid(row=0, column=0, padx=(10, 0))
        self.PNA_seats_spinbox.set("0")
        self.PNA_seats_spinbox.bind("<FocusOut>", spin_box_focus_out)

        # seats availability (row 0, column 1)
        self.PNA_seats_available_label = Label(self.PNA_seats_frame, text=f"Seats ({self.PNA_available_seats} available)", font="Helvetica 12", justify=RIGHT, bg=gold, fg=white, padx=10)
        self.PNA_seats_available_label.grid(row=0, column=1)

        # line seperation (row 3)
        self.PNA_separator = Frame(self.PNA_frame, bg=white, height=2)
        self.PNA_separator.grid(row=3, sticky="ew")

        # PN -> A spinbox & availability for beds
        # frame (row 4)
        self.PNA_beds_frame = Frame(self.PNA_frame, background=gold, borderwidth=0)
        self.PNA_beds_frame.grid(row=4, pady=(7, 5))

        # spinbox (row 0, column 0)
        validate_PNA_beds = parent.register(lambda P: validate_spinbox(P, self.PNA_available_beds))
        self.PNA_beds_spinbox = ttk.Spinbox(self.PNA_beds_frame, width=2, style='amount.TSpinbox', justify=RIGHT, font="Helvetica 12", from_=0, to=self.PNA_available_beds, validate="key", validatecommand=(validate_PNA_beds, '%P'))
        self.PNA_beds_spinbox.grid(row=0, column=0, padx=(10, 0))
        self.PNA_beds_spinbox.set("0")
        self.PNA_beds_spinbox.bind("<FocusOut>", spin_box_focus_out)

        # beds availability (row 0, column 1)
        self.PNA_beds_available_label = Label(self.PNA_beds_frame, text=f"Beds ({self.PNA_available_beds} available)", font="Helvetica 12", justify=RIGHT, bg=gold, fg=white, padx=10)
        self.PNA_beds_available_label.grid(row=0, column=1)



        # A -> PN
        # frame (row 5)
        self.APN_frame = Frame(self.booking_frame, bg=gold, highlightthickness=2, highlightbackground=white)
        self.APN_frame.grid(row=5, pady=10)

        # APN heading (row 0)
        self.APN_heading_label = Label(self.APN_frame, text="Auckland -> Palmerston North", font="Helvetica 12 bold", justify=CENTER, bg=gold, fg=white, padx=10)
        self.APN_heading_label.grid(row=0, pady=(5, 7))

        # line seperation (row 1)
        self.APN_separator = Frame(self.APN_frame, bg=white, height=2)
        self.APN_separator.grid(row=1, sticky="ew")

        # A -> PN spinbox & availability for seats
        # frame (row 2)
        self.APN_seats_frame = Frame(self.APN_frame, background=gold, borderwidth=0)
        self.APN_seats_frame.grid(row=2, pady=(7, 7))

        # spinbox (row 0, column 0)
        validate_APN_seats = parent.register(lambda P: validate_spinbox(P, self.APN_available_seats))
        self.APN_seats_spinbox = ttk.Spinbox(self.APN_seats_frame, width=2, style='amount.TSpinbox', justify=RIGHT, font="Helvetica 12", from_=0, to=self.APN_available_seats, validate="key", validatecommand=(validate_APN_seats, '%P'))
        self.APN_seats_spinbox.grid(row=0, column=0, padx=(10, 0))
        self.APN_seats_spinbox.set("0")
        self.APN_seats_spinbox.bind("<FocusOut>", spin_box_focus_out)

        # seats availability (row 0, column 1)
        self.APN_seats_available_label = Label(self.APN_seats_frame, text=f"Seats ({self.APN_available_seats} available)", font="Helvetica 12", justify=RIGHT, bg=gold, fg=white, padx=10)
        self.APN_seats_available_label.grid(row=0, column=1)

        # line seperation (row 3)
        self.APN_separator = Frame(self.APN_frame, bg=white, height=2)
        self.APN_separator.grid(row=3, sticky="ew")

        # PN -> A spinbox & availability for beds
        # frame (row 4)
        self.APN_beds_frame = Frame(self.APN_frame, background=gold, borderwidth=0)
        self.APN_beds_frame.grid(row=4, pady=(7, 5))

        # spinbox (row 0, column 0)
        validate_APN_beds = parent.register(lambda P: validate_spinbox(P, self.APN_available_beds))
        self.APN_beds_spinbox = ttk.Spinbox(self.APN_beds_frame, width=2, style='amount.TSpinbox', justify=RIGHT, font="Helvetica 12", from_=0, to=self.APN_available_beds, validate="key", validatecommand=(validate_APN_beds, '%P'))
        self.APN_beds_spinbox.grid(row=0, column=0, padx=(10, 0))
        self.APN_beds_spinbox.set("0")
        self.APN_beds_spinbox.bind("<FocusOut>", spin_box_focus_out)

        # beds availability (row 0, column 1)
        self.APN_beds_available_label = Label(self.APN_beds_frame, text=f"Seats ({self.APN_available_beds} available)", font="Helvetica 12", justify=RIGHT, bg=gold, fg=white, padx=10)
        self.APN_beds_available_label.grid(row=0, column=1)

        # error message (row 6)
        self.error_label = Label(self.booking_frame, justify=CENTER, fg=red, bg=blue, text="", font="Helvetica 12 italic")
        self.error_label.grid(row=6, pady=10)

        # Book button (row 7)
        self.book_button = ttk.Button(self.booking_frame, text="Book", style="Book.TButton", command=self.check)
        self.book_button.grid(row=7)

    def check(self):
        error_message = ""
        self.error_label.config(text=error_message)
        pattern = r"^[0-9 +\-]{8,}$"
        name = self.name_entry.get()
        number = self.number_entry.get()
        PNA_seats = int(self.PNA_seats_spinbox.get())
        PNA_beds = int(self.PNA_beds_spinbox.get())
        APN_seats = int(self.APN_seats_spinbox.get())
        APN_beds = int(self.APN_beds_spinbox.get())

        if (name == "Enter your full name") or (len(name) < 3) or (not(" " in name)):
            error_message += "Please check that you have entered\nyour name correctly.\n"

        if not(re.fullmatch(pattern, number)):
            error_message += "Please check that you have entered\nyour phone number correctly.\n"

        if (PNA_seats+PNA_beds+APN_seats+APN_beds) == 0:
            error_message += "Book at least one seat."

        if len(error_message) > 0:
            self.error_label.config(text=error_message)
        else:
            self.confirm()

    def confirm(self):
        self.confirm_window = Confirm(self.booking_frame, self)

    def update_ui(self):
        # 1. PNA Seats
        self.PNA_seats_available_label.config(text=f"Seats ({self.PNA_available_seats} available)")
        self.PNA_seats_spinbox.config(to=self.PNA_available_seats)
        
        # 2. PNA Beds
        self.PNA_beds_available_label.config(text=f"Beds ({self.PNA_available_beds} available)")
        self.PNA_beds_spinbox.config(to=self.PNA_available_beds)

        # 3. APN Seats
        self.APN_seats_available_label.config(text=f"Seats ({self.APN_available_seats} available)")
        self.APN_seats_spinbox.config(to=self.APN_available_seats)

        # 4. APN Beds
        self.APN_beds_available_label.config(text=f"Beds ({self.APN_available_beds} available)")
        self.APN_beds_spinbox.config(to=self.APN_available_beds)
        
        # Spinboxen auf 0 zurücksetzen nach dem Buchen
        self.PNA_seats_spinbox.set("0")
        self.PNA_beds_spinbox.set("0")
        self.APN_seats_spinbox.set("0")
        self.APN_beds_spinbox.set("0")

        self.name_entry.delete(0, "end")
        self.name_entry.insert(0, "Enter your full name")
        self.number_entry.delete(0, "end")
        self.number_entry.insert(0, "Enter your phone number")



















class Confirm:
    def __init__(self, parent, booking):
        # creating colour variables
        white = "#FFFFFF"
        grey = "#E6E6E6"
        blue = "#004B8D"
        gold = "#E4A024"
        red = "#FFCCCC"
        purple = "#9933FF"
        green = "#00CC00"

        self.booking = booking
        self.name = self.booking.name_entry.get()
        self.number = self.booking.number_entry.get()

        self.PNA_seats_amount = int(self.booking.PNA_seats_spinbox.get())
        self.PNA_beds_amount = int(self.booking.PNA_beds_spinbox.get())
        self.APN_seats_amount = int(self.booking.APN_seats_spinbox.get())
        self.APN_beds_amount = int(self.booking.APN_beds_spinbox.get())
        self.PNA_seats_price = self.PNA_seats_amount*25
        self.PNA_beds_price = self.PNA_beds_amount*50
        self.APN_seats_price = self.APN_seats_amount*25
        self.APN_beds_price = self.APN_beds_amount*50

        self.total = self.PNA_seats_price + self.PNA_beds_price + self.APN_seats_price + self.APN_beds_price
        self.gst_portion = round((self.total - (self.total/1.15)), 2)

        self.PNA_available_seats = self.booking.PNA_available_seats
        self.PNA_available_beds = self.booking.PNA_available_beds
        self.APN_available_seats = self.booking.APN_available_seats
        self.APN_available_beds = self.booking.APN_available_beds

        # get the main window
        self.main_window = parent.winfo_toplevel()

        # grey transparent overlay without title bar
        self.overlay = Toplevel(self.main_window)
        self.overlay.configure(bg="grey")
        self.overlay.attributes("-alpha", 0.5)
        self.overlay.overrideredirect(True)
        self.overlay.geometry(f"{self.main_window.winfo_width()}x" f"{self.main_window.winfo_height()}+" f"{self.main_window.winfo_rootx()}+" f"{self.main_window.winfo_rooty()-32}")

        # child window
        self.confirm_box = Toplevel()

        # confirm frame
        self.confirm_frame = Frame(self.confirm_box, bg=gold, pady=10)
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

        self.total_gst_frame.columnconfigure(0, weight=1)
        self.total_gst_frame.columnconfigure(1, weight=0, minsize=2)
        self.total_gst_frame.columnconfigure(2, weight=1)

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

        self.edit_save_frame.columnconfigure(0, weight=1)
        self.edit_save_frame.columnconfigure(1, weight=0, minsize=2)
        self.edit_save_frame.columnconfigure(2, weight=1)

    def edit(self):
        self.overlay.destroy()
        self.confirm_box.destroy()

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

        self.booking.PNA_available_seats -= PNA_seats_amount
        self.booking.PNA_available_beds -= PNA_beds_amount
        self.booking.APN_available_seats -= APN_seats_amount
        self.booking.APN_available_beds -= APN_beds_amount

        self.booking.update_ui()
        self.overlay.destroy()
        self.confirm_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.configure()
    root.title("Go Bus Booking")
    something = Booking(root)
    root.mainloop()