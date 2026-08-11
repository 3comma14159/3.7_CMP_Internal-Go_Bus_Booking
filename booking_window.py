from tkinter import *
from tkinter import ttk
import re

class Booking:
    def __init__(self, parent):
        # creating colour variables
        white = "#FFFFFF"
        grey = "#E6E6E6"
        blue = "#004B8D"
        gold = "#E4A024"
        red = "#FFCCCC"

        PNA_available_seats = 20
        PNA_available_beds = 15

        APN_available_seats = 20
        APN_available_beds = 15

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
        placeholder_setup(self.name_entry, "Enter your name")

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
        validate_PNA_seats = parent.register(lambda P: validate_spinbox(P, PNA_available_seats))
        self.PNA_seats_spinbox = ttk.Spinbox(self.PNA_seats_frame, width=2, style='amount.TSpinbox', justify=RIGHT, font="Helvetica 12", from_=0, to=PNA_available_seats, validate="key", validatecommand=(validate_PNA_seats, '%P'))
        self.PNA_seats_spinbox.grid(row=0, column=0, padx=(10, 0))
        self.PNA_seats_spinbox.set("0")
        self.PNA_seats_spinbox.bind("<FocusOut>", spin_box_focus_out)

        # seats availability (row 0, column 1)
        self.PNA_seats_available_label = Label(self.PNA_seats_frame, text=f"Seats ({PNA_available_seats} available)", font="Helvetica 12", justify=RIGHT, bg=gold, fg=white, padx=10)
        self.PNA_seats_available_label.grid(row=0, column=1)

        # line seperation (row 3)
        self.PNA_separator = Frame(self.PNA_frame, bg=white, height=2)
        self.PNA_separator.grid(row=3, sticky="ew")

        # PN -> A spinbox & availability for beds
        # frame (row 4)
        self.PNA_beds_frame = Frame(self.PNA_frame, background=gold, borderwidth=0)
        self.PNA_beds_frame.grid(row=4, pady=(7, 5))

        # spinbox (row 0, column 0)
        validate_PNA_beds = parent.register(lambda P: validate_spinbox(P, PNA_available_beds))
        self.PNA_beds_spinbox = ttk.Spinbox(self.PNA_beds_frame, width=2, style='amount.TSpinbox', justify=RIGHT, font="Helvetica 12", from_=0, to=PNA_available_beds, validate="key", validatecommand=(validate_PNA_beds, '%P'))
        self.PNA_beds_spinbox.grid(row=0, column=0, padx=(10, 0))
        self.PNA_beds_spinbox.set("0")
        self.PNA_beds_spinbox.bind("<FocusOut>", spin_box_focus_out)

        # beds availability (row 0, column 1)
        self.PNA_beds_available_label = Label(self.PNA_beds_frame, text=f"Seats ({PNA_available_beds} available)", font="Helvetica 12", justify=RIGHT, bg=gold, fg=white, padx=10)
        self.PNA_beds_available_label.grid(row=0, column=1)



        # PN -> A
        # frame (row 5)
        self.APN_frame = Frame(self.booking_frame, bg=gold, highlightthickness=2, highlightbackground=white)
        self.APN_frame.grid(row=5, pady=10)

        # APN heading (row 0)
        self.APN_heading_label = Label(self.APN_frame, text="Palmerston North -> Auckland", font="Helvetica 12 bold", justify=CENTER, bg=gold, fg=white, padx=10)
        self.APN_heading_label.grid(row=0, pady=(5, 7))

        # line seperation (row 1)
        self.APN_separator = Frame(self.APN_frame, bg=white, height=2)
        self.APN_separator.grid(row=1, sticky="ew")

        # PN -> A spinbox & availability for seats
        # frame (row 2)
        self.APN_seats_frame = Frame(self.APN_frame, background=gold, borderwidth=0)
        self.APN_seats_frame.grid(row=2, pady=(7, 7))

        # spinbox (row 0, column 0)
        validate_APN_seats = parent.register(lambda P: validate_spinbox(P, APN_available_seats))
        self.APN_seats_spinbox = ttk.Spinbox(self.APN_seats_frame, width=2, style='amount.TSpinbox', justify=RIGHT, font="Helvetica 12", from_=0, to=APN_available_seats, validate="key", validatecommand=(validate_APN_seats, '%P'))
        self.APN_seats_spinbox.grid(row=0, column=0, padx=(10, 0))
        self.APN_seats_spinbox.set("0")
        self.APN_seats_spinbox.bind("<FocusOut>", spin_box_focus_out)

        # seats availability (row 0, column 1)
        self.APN_seats_available_label = Label(self.APN_seats_frame, text=f"Seats ({APN_available_seats} available)", font="Helvetica 12", justify=RIGHT, bg=gold, fg=white, padx=10)
        self.APN_seats_available_label.grid(row=0, column=1)

        # line seperation (row 3)
        self.APN_separator = Frame(self.APN_frame, bg=white, height=2)
        self.APN_separator.grid(row=3, sticky="ew")

        # PN -> A spinbox & availability for beds
        # frame (row 4)
        self.APN_beds_frame = Frame(self.APN_frame, background=gold, borderwidth=0)
        self.APN_beds_frame.grid(row=4, pady=(7, 5))

        # spinbox (row 0, column 0)
        validate_APN_beds = parent.register(lambda P: validate_spinbox(P, APN_available_beds))
        self.APN_beds_spinbox = ttk.Spinbox(self.APN_beds_frame, width=2, style='amount.TSpinbox', justify=RIGHT, font="Helvetica 12", from_=0, to=APN_available_beds, validate="key", validatecommand=(validate_APN_beds, '%P'))
        self.APN_beds_spinbox.grid(row=0, column=0, padx=(10, 0))
        self.APN_beds_spinbox.set("0")
        self.APN_beds_spinbox.bind("<FocusOut>", spin_box_focus_out)

        # beds availability (row 0, column 1)
        self.APN_beds_available_label = Label(self.APN_beds_frame, text=f"Seats ({APN_available_beds} available)", font="Helvetica 12", justify=RIGHT, bg=gold, fg=white, padx=10)
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

        if name == "Enter your name" or len(name) < 3:
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
        self.confirm_window = Confirm(self.booking_frame)
        
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

# main routine
if __name__ == "__main__":
    root = Tk()
    root.configure()
    root.title("Go Bus Booking")
    something = Booking(root)
    root.mainloop()