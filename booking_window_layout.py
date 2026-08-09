from tkinter import *

class Booking:
    def __init__(self, parent):
        # creating colour variables
        font = "#FFFFFF"
        blue = "#004B8D"
        gold = "#E4A024"
        red = "#FFCCCC"
        purple = "#9933FF"
        green = "#00CC00"

        # booking frame
        self.booking_frame = Frame(bg=blue, pady=10)
        self.booking_frame.grid()

        # heading (row 0)
        self.book_heading_label = Label(self.booking_frame, text="Go Bus Booking", font="Helvetica 20 bold", bg=blue, fg=font, padx=10, pady=10)
        self.book_heading_label.grid(row=0)

        # instructions (row 1)
        self.book_instructions_label = Label(self.booking_frame, text="Instructions", font="Helvetica 12 italic", bg=blue, fg=font, pady=10, padx=10)
        self.book_instructions_label.grid(row=1)

        # name input (row 2) - put entry box in a frame to have more style options
        self.book_name_frame = Frame(self.booking_frame, bg=gold, borderwidth=0, highlightthickness=2, highlightbackground=font)
        self.book_name_frame.grid(row=2, padx=20, pady=5)
        
        self.book_name_entry = Entry(self.book_name_frame, font="Helvetica 14", bg=gold, fg=font, highlightthickness=0, bd=0)
        self.book_name_entry.grid(padx=10, pady=5)

        # phone number input (row 3) - put entry box in a frame to have more style options
        self.book_number_frame = Frame(self.booking_frame, bg=gold, borderwidth=0, highlightthickness=2, highlightbackground=font)
        self.book_number_frame.grid(row=3, padx=20, pady=5)
                
        self.book_number_entry = Entry(self.book_number_frame, font="Helvetica 14", bg=gold, fg=font, highlightthickness=0, bd=0)
        self.book_number_entry.grid(padx=10, pady=5)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.configure()
    root.title("Go Bus Booking")
    something = Booking(root)
    root.mainloop()