from tkinter import *
import tkinter as tk
from tkinter import ttk
import re

# window in which booking and confirm page are shown
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Go Bus Booking')

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.booking_page = Booking(self)
        self.booking_page.grid(row=0, column=0, sticky="nsew")

        self.confirm_page = Confirm(self, self.booking_page)
        self.confirm_page.grid(row=0, column=0, sticky="nsew")

        # prepare text file
        f = open("go_bus_booking.txt", "w+")
        f.truncate(0)
        f.seek(0)
        f.write("Every line is one booking. The information is written the following way: Name, number, PNA seats amount, PNA beds amount, APN seats amoung, APN beds amount, total price, gst portion\n")
        f.close()

        self.show_booking_page()

    # show booking page through raising it up
    def show_booking_page(self):
        self.booking_page.tkraise()

    # show confirm page through raising it up and update shown values
    def show_confirm_page(self):
        self.confirm_page.update_ui()
        self.confirm_page.tkraise()

# booking page
class Booking(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#004B8D", pady=10)
        self.parent = parent

        # Centre the complete Booking page inside the application window.
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.booking_content = Frame(self, bg="#004B8D")
        self.booking_content.grid(row=0, column=0)

        # -------------------------------------------------------------------------------------------------------
        #                                   Preparation (Variables, Styles, Functions)
        # -------------------------------------------------------------------------------------------------------
        

        # Variables -------------------------------------------------------------------------------------------------------

        # creating colour variables
        white = "#FFFFFF"
        grey = "#E6E6E6"
        blue = "#004B8D"
        gold = "#E4A024"
        red = "#FFCCCC"

        # seats availability varibales
        self.PNA_available_seats = 20
        self.PNA_available_beds = 15
        self.APN_available_seats = 20
        self.APN_available_beds = 15


        # Styling -------------------------------------------------------------------------------------------------------

        # for button and spinbox styling
        self.style = ttk.Style()
        self.style.theme_use('clam')

        # spinbox style
        self.style.configure('amount.TSpinbox', fieldbackground=gold, background=gold, arrowcolor=blue, foreground=white, bordercolor=gold, lightcolor=gold, darkcolor=gold)
        self.style.map('amount.TSpinbox', bordercolor=[('focus', gold)], lightcolor=[('focus', gold)], darkcolor=[('focus', gold)], fieldbackground=[('focus', gold)], foreground=[('focus', white)], selectbackground=[('focus', gold), ('!focus', gold)], selectforeground=[('focus', white), ('!focus', white)])

        # book button style
        self.style.configure('Book.TButton', background=gold, foreground=white, font="Helvetica 16 bold", padding=(10, 5), borderwidth=4, bordercolor=gold, lightcolor=gold, darkcolor=gold, focuscolor=gold)
        self.style.map('Book.TButton', background=[('active', gold), ('pressed', gold)], foreground=[('active', white), ('pressed', white)], bordercolor=[('active', white), ('pressed', white)], lightcolor=[('active', white), ('pressed', white)], darkcolor=[('active', white), ('pressed', white)], focuscolor=[('active', gold), ('pressed', gold)])


        # Functions -------------------------------------------------------------------------------------------------------

        # placeholder for name and phone number entry fields when field is empty - called once from name and phone number entry
        def placeholder_setup(entry, placeholder):
            # placeholder text displayed in grey
            entry.insert(0, placeholder)
            entry.config(fg=grey)

            # no entry yet -> placeholder is removed - called when field is clicked
            def clear_placeholder(event):
                if event.widget.get() == placeholder:
                    event.widget.delete(0, "end")
                    event.widget.config(fg=white)

            # no entry yet -> placeholder is added - called when field is left
            def add_placeholder(event):
                if len(event.widget.get()) == 0:
                    event.widget.insert(0, placeholder)
                    event.widget.config(fg=grey)

            # when field clicked or left, placeholder clear and add functions are called
            entry.bind("<FocusIn>", clear_placeholder)
            entry.bind("<FocusOut>", add_placeholder)

        # validation spinbox input - called when spin box input changed
        def validate_spinbox(new_value, limit):
            # allows only numeric input within availability range or delete or empty field
            if (new_value.isdigit() and int(new_value)<=limit) or new_value == "":
                return True
            return False

        # empty spinbox -> 0 inserted - called when spin box left
        def spin_box_focus_out(event):
            if event.widget.get() == "":
                event.widget.delete(0, "end")
                event.widget.insert(0, "0")



        # -------------------------------------------------------------------------------------------------------
        #                                   heading, instructions, name and number input
        # -------------------------------------------------------------------------------------------------------

        # heading (row 0)
        self.heading_label = Label(self.booking_content, text="Go Bus Booking", font="Helvetica 20 bold", bg=blue, fg=white, padx=10, pady=10)
        self.heading_label.grid(row=0)

        # instructions (row 1)
        self.instructions_label = Label(self.booking_content, text="Please enter your full name, phone number\nand the amount of tickets you want to buy.\nThe following prices include GST:\nA seat costs $25 and a bed costs $50.", font="Helvetica 12 italic", bg=blue, fg=white, pady=10, padx=10)
        self.instructions_label.grid(row=1)

        # name input (row 2) - put entry box in a frame to have more style options
        self.name_frame = Frame(self.booking_content, bg=gold, borderwidth=0, highlightthickness=2, highlightbackground=white)
        self.name_frame.grid(row=2, padx=20, pady=5)
        
        self.name_entry = Entry(self.name_frame, font="Helvetica 14", bg=gold, fg=white, highlightthickness=0, bd=0)
        self.name_entry.grid(padx=12, pady=5)
        placeholder_setup(self.name_entry, "Enter your full name")

        # phone number input (row 3) - put entry box in a frame to have more style options
        self.number_frame = Frame(self.booking_content, bg=gold, borderwidth=0, highlightthickness=2, highlightbackground=white)
        self.number_frame.grid(row=3, padx=20, pady=5)
                
        self.number_entry = Entry(self.number_frame, font="Helvetica 14", bg=gold, fg=white, highlightthickness=0, bd=0)
        self.number_entry.grid(padx=12, pady=5)
        placeholder_setup(self.number_entry, "Enter your phone number")



        # -------------------------------------------------------------------------------------------------------
        #                                   PN -> A table
        # -------------------------------------------------------------------------------------------------------

        # frame (row 4)
        self.PNA_frame = Frame(self.booking_content, bg=gold, highlightthickness=2, highlightbackground=white)
        self.PNA_frame.grid(row=4, pady=(20, 10))

        # PNA heading (row 0)
        self.PNA_heading_label = Label(self.PNA_frame, text="Palmerston North -> Auckland", font="Helvetica 12 bold", justify=CENTER, bg=gold, fg=white, padx=10)
        self.PNA_heading_label.grid(row=0, pady=(5, 7))

        # line seperation (row 1)
        self.PNA_separator = Frame(self.PNA_frame, bg=white, height=2)
        self.PNA_separator.grid(row=1, sticky="ew")


        # PN -> A seats row -------------------------------------------------------------------------------------------------------

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


        # PN -> A beds row -------------------------------------------------------------------------------------------------------

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



        # -------------------------------------------------------------------------------------------------------
        #                                   A -> PN table
        # -------------------------------------------------------------------------------------------------------

        # frame (row 5)
        self.APN_frame = Frame(self.booking_content, bg=gold, highlightthickness=2, highlightbackground=white)
        self.APN_frame.grid(row=5, pady=10)

        # APN heading (row 0)
        self.APN_heading_label = Label(self.APN_frame, text="Auckland -> Palmerston North", font="Helvetica 12 bold", justify=CENTER, bg=gold, fg=white, padx=10)
        self.APN_heading_label.grid(row=0, pady=(5, 7))

        # line seperation (row 1)
        self.APN_separator = Frame(self.APN_frame, bg=white, height=2)
        self.APN_separator.grid(row=1, sticky="ew")


        # A -> PN seats row -------------------------------------------------------------------------------------------------------

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


        # A -> PN beds row -------------------------------------------------------------------------------------------------------
        
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



        # -------------------------------------------------------------------------------------------------------
        #                                   Error message, book button
        # -------------------------------------------------------------------------------------------------------

        # error message (row 6)
        self.error_label = Label(self.booking_content, justify=CENTER, fg=red, bg=blue, text="", font="Helvetica 12 italic")
        self.error_label.grid(row=6, pady=10)

        # Book button (row 7)
        self.book_button = ttk.Button(self.booking_content, text="Book", style="Book.TButton", command=self.check)
        self.book_button.grid(row=7)



    # -------------------------------------------------------------------------------------------------------
    #                                   Functions
    # -------------------------------------------------------------------------------------------------------

    # check booking - called from booking button
    def check(self):
        # preparation of error message
        error_message = ""
        self.error_label.config(text=error_message)

        # get inputs
        name = self.name_entry.get()
        number = self.number_entry.get().strip()
        PNA_seats = int(self.PNA_seats_spinbox.get())
        PNA_beds = int(self.PNA_beds_spinbox.get())
        APN_seats = int(self.APN_seats_spinbox.get())
        APN_beds = int(self.APN_beds_spinbox.get())

        # check that name has been entered and is at least one character, a space and at least another character
        if (name == "Enter your full name") or (not(re.fullmatch("^.+\s.+$", name))):
            error_message += "Please check that you have entered\nyour name correctly.\n"

        # check that the number has max one plus at the beginning, between 4 and 18 numbers (0-9) and as many " ", "-" or "/" as the user wants
        if not(re.fullmatch("^\+?(?=(?:\D*\d){4,18}\D*$)[0-9\- /]+$", number)):
            error_message += "Please check that you have entered\nyour phone number correctly.\n"
        
        # checks that at least one seat is booked
        if (PNA_seats+PNA_beds+APN_seats+APN_beds) == 0:
            error_message += "Book at least one seat."

        # if error detected, the message is displayed, otherwise confirm page is opened
        if len(error_message) > 0:
            self.error_label.config(text=error_message)
        else:
            self.parent.show_confirm_page()

    # reset booking page - called from Confirm page Save button
    def update_ui(self):
        # update seats availability
        self.PNA_seats_available_label.config(text=f"Seats ({self.PNA_available_seats} available)")
        self.PNA_seats_spinbox.config(to=self.PNA_available_seats)
        self.PNA_beds_available_label.config(text=f"Beds ({self.PNA_available_beds} available)")
        self.PNA_beds_spinbox.config(to=self.PNA_available_beds)
        self.APN_seats_available_label.config(text=f"Seats ({self.APN_available_seats} available)")
        self.APN_seats_spinbox.config(to=self.APN_available_seats)
        self.APN_beds_available_label.config(text=f"Beds ({self.APN_available_beds} available)")
        self.APN_beds_spinbox.config(to=self.APN_available_beds)
        
        # reset spinboxes to 0
        self.PNA_seats_spinbox.set("0")
        self.PNA_beds_spinbox.set("0")
        self.APN_seats_spinbox.set("0")
        self.APN_beds_spinbox.set("0")

        # empty name and number entry field and replace with placeholders
        self.name_entry.delete(0, "end")
        self.name_entry.insert(0, "Enter your full name")
        self.number_entry.delete(0, "end")
        self.number_entry.insert(0, "Enter your phone number")

# confirm page
class Confirm(Frame):
    def __init__(self, parent, booking):
        super().__init__(parent, bg="#E4A024", pady=10)
        self.parent = parent
        self.booking = booking



        # -------------------------------------------------------------------------------------------------------
        #                                   Preparation (Variables, Styles)
        # -------------------------------------------------------------------------------------------------------

        # creating colour variables
        white = "#FFFFFF"
        grey = "#E6E6E6"
        blue = "#004B8D"
        gold = "#E4A024"
        red = "#FFCCCC"
        purple = "#9933FF"
        green = "#00CC00"

        # getting all the necessary variables from Confirm window, updated by update_ui() when confirmation page opened
        self.name = ""
        self.number = ""
        self.PNA_seats_amount = 0
        self.PNA_beds_amount = 0
        self.APN_seats_amount = 0
        self.APN_beds_amount = 0
        self.PNA_seats_price = 0
        self.PNA_beds_price = 0
        self.APN_seats_price = 0
        self.APN_beds_price = 0
        self.total = 0
        self.gst_portion = 0

        # for button styling
        self.style = ttk.Style()
        self.style.theme_use('clam')

        # edit button style
        self.style.configure('Edit.TButton', background=purple, focuscolor=purple, foreground=white, font="Helvetica 16 bold", padding=(10, 5), borderwidth=0) #focus color
        self.style.map('Edit.TButton', background=[('active', purple), ('pressed', purple)], foreground=[('active', white), ('pressed', white)], focuscolor=[('active', purple), ('pressed', purple)])

        # save button style
        self.style.configure('Save.TButton', background=green, focuscolor=green, foreground=white, font="Helvetica 16 bold", padding=(10, 5), borderwidth=0) #focus color
        self.style.map('Save.TButton', background=[('active', green), ('pressed', green)], foreground=[('active', white), ('pressed', white)], focuscolor=[('active', green), ('pressed', green)])
        


        # -------------------------------------------------------------------------------------------------------
        #                                  heading, instructions, name, number
        # -------------------------------------------------------------------------------------------------------

        # heading (row 0)
        self.heading_label = Label(self, text="Your Booking", font="Helvetica 20 bold", bg=gold, fg=white, padx=10, pady=10)
        self.heading_label.grid(row=0)

        # instructions (row 1)
        self.instructions_label = Label(self, text="Please check your name, number and booking.", font="Helvetica 12 italic", bg=gold, fg=white, pady=10, padx=10)
        self.instructions_label.grid(row=1)

        # name (row 2)
        self.name_label = Label(self, bg=blue, fg=white, text=f"Name: {self.name}", font="Helvetica 14", anchor="w", highlightthickness=2, highlightbackground=white, relief="flat", padx=12, pady=5)
        self.name_label.grid(row=2, padx=20, pady=5, sticky="ew")

        # number (row 3)
        self.number_label = Label(self, bg=blue, fg=white, text=f"Number: {self.number}", font="Helvetica 14", anchor="w", highlightthickness=2, highlightbackground=white, relief="flat", padx=12, pady=5)
        self.number_label.grid(row=3, padx=20, pady=5, sticky="ew")



        # -------------------------------------------------------------------------------------------------------
        #                                   PN -> A table
        # -------------------------------------------------------------------------------------------------------

        # PNA frame (row 4)
        self.PNA_frame = Frame(self, bg=blue, highlightthickness=2, highlightbackground=white)
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


        # specifying column widths -------------------------------------------------------------------------------------------------------

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
        self.APN_frame = Frame(self, bg=blue, highlightthickness=2, highlightbackground=white)
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


        # specifying column widths -------------------------------------------------------------------------------------------------------

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
        self.total_gst_frame = Frame(self, bg=blue, highlightthickness=2, highlightbackground=white)
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

        # configure column widths
        self.total_gst_frame.columnconfigure(0, weight=1)
        self.total_gst_frame.columnconfigure(1, weight=0, minsize=2)
        self.total_gst_frame.columnconfigure(2, weight=1)


        # Buttons -------------------------------------------------------------------------------------------------------

        # edit, save buttons frame (row 7)
        self.edit_save_frame = Frame(self, bg=blue, highlightthickness=2, highlightbackground=white)
        self.edit_save_frame.grid(row=7, padx=20, pady=10, sticky="ew")

        # edit button (row 0, col 0)
        self.edit_button = ttk.Button(self.edit_save_frame, text="Edit", style="Edit.TButton", command=self.edit)
        self.edit_button.grid(row=0, column=0, sticky="ew")

        # separator (row 0, col 1)
        self.edit_save_separator = Frame(self.edit_save_frame, bg=white, width=2)
        self.edit_save_separator.grid(row=0, column=1, sticky="ns")

        # save button (row 0, col 2)
        self.save_button = ttk.Button(self.edit_save_frame, text="Save", style="Save.TButton", command=self.save)
        self.save_button.grid(row=0, column=2, sticky="ew")

        # configure column widths
        self.edit_save_frame.columnconfigure(0, weight=1)
        self.edit_save_frame.columnconfigure(1, weight=0, minsize=2)
        self.edit_save_frame.columnconfigure(2, weight=1)



    # -------------------------------------------------------------------------------------------------------
    #                                   Functions
    # -------------------------------------------------------------------------------------------------------
    
    # update values on Confirm Page whenever raised to top
    def update_ui(self):
        # get current values from the Booking page
        self.name = self.booking.name_entry.get()
        self.number = self.booking.number_entry.get()
        self.PNA_seats_amount = int(self.booking.PNA_seats_spinbox.get())
        self.PNA_beds_amount = int(self.booking.PNA_beds_spinbox.get())
        self.APN_seats_amount = int(self.booking.APN_seats_spinbox.get())
        self.APN_beds_amount = int(self.booking.APN_beds_spinbox.get())

        # Calculate prices
        self.PNA_seats_price = self.PNA_seats_amount * 25
        self.PNA_beds_price = self.PNA_beds_amount * 50
        self.APN_seats_price = self.APN_seats_amount * 25
        self.APN_beds_price = self.APN_beds_amount * 50

        self.total = (self.PNA_seats_price + self.PNA_beds_price + self.APN_seats_price + self.APN_beds_price)
        self.gst_portion = round(self.total - (self.total / 1.15), 2)

        # Update every value displayed on the confirmation page
        self.name_label.config(text=f"Name: {self.name}")
        self.number_label.config(text=f"Number: {self.number}")
        self.PNA_seats_number_label.config(text=self.PNA_seats_amount)
        self.PNA_seats_price_label.config(text=f"${self.PNA_seats_price}")
        self.PNA_beds_number_label.config(text=self.PNA_beds_amount)
        self.PNA_beds_price_label.config(text=f"${self.PNA_beds_price}")
        self.APN_seats_number_label.config(text=self.APN_seats_amount)
        self.APN_seats_price_label.config(text=f"${self.APN_seats_price}")
        self.APN_beds_number_label.config(text=self.APN_beds_amount)
        self.APN_beds_price_label.config(text=f"${self.APN_beds_price}")
        self.total_label.config(text=f"Total: ${self.total}")
        self.gst_label.config(text=f"GST Portion: ${self.gst_portion}")

    # return to booking page - called from Edit button
    def edit(self):
        self.parent.show_booking_page()

    # everything needed to complete booking - called from Save button
    def save(self):
        # get values from Confirm page
        name = self.name
        number = self.number
        PNA_seats_amount = self.PNA_seats_amount
        PNA_beds_amount = self.PNA_beds_amount
        APN_seats_amount = self.APN_seats_amount
        APN_beds_amount = self.APN_beds_amount
        total = self.total
        gst = self.gst_portion

        # prepare text for text file and add it
        text = f"{name}, {number}, {PNA_seats_amount}, {PNA_beds_amount}, {APN_seats_amount}, {APN_beds_amount}, {total}, {gst}"
        f = open("go_bus_booking.txt", "a")
        f.write(text + "\n")
        f.close()

        # update amount of available seats
        self.booking.PNA_available_seats -= PNA_seats_amount
        self.booking.PNA_available_beds -= PNA_beds_amount
        self.booking.APN_available_seats -= APN_seats_amount
        self.booking.APN_available_beds -= APN_beds_amount

        # reset booking page ui and raise it to top
        self.booking.update_ui()
        self.parent.show_booking_page()

# main routine
if __name__ == "__main__":
    app = App()
    app.mainloop()