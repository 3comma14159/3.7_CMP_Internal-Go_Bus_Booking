from tkinter import *

class Booking:
    def __init__(self, parent):
        # creating colour variables
        white = "#FFFFFF"
        grey = "#E6E6E6"
        blue = "#004B8D"
        gold = "#E4A024"
        red = "#FFCCCC"
        purple = "#9933FF"
        green = "#00CC00"

        def placeholder_setup(entry, placeholder):
            entry.insert(0, placeholder)
            entry.config(fg=grey)
                
            def clear_placeholder(event):
                if event.widget.get() == placeholder:
                    event.widget.delete(0, "end")
                    event.widget.config(fg=white)
            
            def add_placeholder(event):
                if len(event.widget.get()) == 0:
                    event.widget.insert(0, placeholder)
                    event.widget.config(fg=grey)
                
            entry.bind("<FocusIn>", clear_placeholder)
            entry.bind("<FocusOut>", add_placeholder)
        

        # booking frame
        self.booking_frame = Frame(bg=blue, pady=10)
        self.booking_frame.grid()

        # heading (row 0)
        self.book_heading_label = Label(self.booking_frame, text="Go Bus Booking", font="Helvetica 20 bold", bg=blue, fg=white, padx=10, pady=10)
        self.book_heading_label.grid(row=0)

        # instructions (row 1)
        self.book_instructions_label = Label(self.booking_frame, text="Please enter your name, phone number\nand the amount of tickets you want to buy.\nThe following prices include GST:\nA seat costs $25 and a bed costs $50.", font="Helvetica 12 italic", bg=blue, fg=white, pady=10, padx=10)
        self.book_instructions_label.grid(row=1)

        # name input (row 2) - put entry box in a frame to have more style options
        self.book_name_frame = Frame(self.booking_frame, bg=gold, borderwidth=0, highlightthickness=2, highlightbackground=white)
        self.book_name_frame.grid(row=2, padx=20, pady=5)
        
        self.book_name_entry = Entry(self.book_name_frame, font="Helvetica 14", bg=gold, fg=white, highlightthickness=0, bd=0)
        self.book_name_entry.grid(padx=10, pady=5)
        placeholder_setup(self.book_name_entry, "Enter your name")

        # phone number input (row 3) - put entry box in a frame to have more style options
        self.book_number_frame = Frame(self.booking_frame, bg=gold, borderwidth=0, highlightthickness=2, highlightbackground=white)
        self.book_number_frame.grid(row=3, padx=20, pady=5)
                
        self.book_number_entry = Entry(self.book_number_frame, font="Helvetica 14", bg=gold, fg=white, highlightthickness=0, bd=0)
        self.book_number_entry.grid(padx=10, pady=5)
        placeholder_setup(self.book_number_entry, "Enter your phone number")

# main routine
if __name__ == "__main__":
    root = Tk()
    root.configure()
    root.title("Go Bus Booking")
    something = Booking(root)
    root.mainloop()