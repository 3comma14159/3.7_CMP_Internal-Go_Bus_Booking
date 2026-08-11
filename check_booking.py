import re

def check():
    error_message = ""
    pattern = r"^[0-9 +\-]{8,}$"
    name = "name"
    number = "34567890-"
    PNA_seats = 0
    PNA_beds = 1
    APN_seats = 0
    APN_beds = 0

    if name == "Enter your name" or len(name) < 3:
        error_message += "Please check that you have entered your name correctly.\n"

    if not(re.fullmatch(pattern, number)):
        error_message += "Please check that you have entered your phone number correctly.\n"

    if (PNA_seats+PNA_beds+APN_seats+APN_beds) == 0:
        error_message += "Book at least one seat."

    if len(error_message) > 0:
        print(error_message)
    else:
        print("passed")
        
check()