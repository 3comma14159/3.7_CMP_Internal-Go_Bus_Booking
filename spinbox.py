from tkinter import *

class spin_box:
    def __init__(self, parent):
        # frame
        self.booking_frame = Frame()
        self.booking_frame.grid()

        available = 10

        # Validation function to check if input is numeric and within amount of available seats/beds or empty
        def validate_spinbox(new_value):
            if (new_value.isdigit() and int(new_value)<=available) or new_value == "":
                return True
            return False

        # spinbox 1
        self.spinbox = Spinbox(self.booking_frame, from_=0, to=available, validate="key", validatecommand=(parent.register(validate_spinbox), '%P'))
        self.spinbox.grid(padx=20, pady=20)

        # spinbox 2
        self.spinbox_2 = Spinbox(self.booking_frame, from_=0, to=available, validate="key", validatecommand=(parent.register(validate_spinbox), '%P'))
        self.spinbox_2.grid(padx=20, pady=20)

        # empty inbox -> 0 inserted
        def spin_box_focus_out(event):
            if event.widget.get() == "":
                event.widget.delete(0, "end")
                event.widget.insert(0, "0")

        # spinbox field exited -> calls function to check if spinbox empty
        self.spinbox.bind("<FocusOut>", spin_box_focus_out)
        self.spinbox_2.bind("<FocusOut>", spin_box_focus_out)

if __name__ == "__main__":
    root = Tk()
    root.configure()
    root.title("")
    something = spin_box(root)
    root.mainloop()