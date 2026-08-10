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
                print(event.widget.get())
                if event.widget.get() == placeholder:
                    event.widget.delete(0, "end")
                    event.config(fg=white)
            
            def add_placeholder(event):
                if len(event.widget.get()) == 0:
                    event.widget.insert(0, placeholder)
                    event.config(fg=grey)
                
            entry.bind("<FocusIn>", clear_placeholder)
            entry.bind("<FocusOut>", add_placeholder)

        # booking frame
        self.booking_frame = Frame(bg=blue, pady=10)
        self.booking_frame.grid()

        # name input (row 0) - put entry box in a frame to have more style options
        self.book_name_frame = Frame(self.booking_frame, bg=gold, borderwidth=0, highlightthickness=2, highlightbackground=white)
        self.book_name_frame.grid(row=0, padx=20, pady=5)
        
        self.book_name_entry = Entry(self.book_name_frame, font="Helvetica 12", bg=gold, fg=white, highlightthickness=0, bd=0)
        self.book_name_entry.grid(padx=10, pady=5)
        placeholder_setup(self.book_name_entry, "Enter your name")

        # phone number input (row 1) - put entry box in a frame to have more style options
        self.book_number_frame = Frame(self.booking_frame, bg=gold, borderwidth=0, highlightthickness=2, highlightbackground=white)
        self.book_number_frame.grid(row=1, padx=20, pady=5)
                
        self.book_number_entry = Entry(self.book_number_frame, font="Helvetica 12", bg=gold, fg=white, highlightthickness=0, bd=0)
        self.book_number_entry.grid(padx=10, pady=5)
        placeholder_setup(self.book_number_entry, "Enter your phone number")

# main routine
if __name__ == "__main__":
    root = Tk()
    root.configure()
    root.title("Go Bus Booking")
    something = Booking(root)
    root.mainloop()