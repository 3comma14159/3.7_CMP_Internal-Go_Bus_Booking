PNA_seats = 20
PNA_beds = 15
APN_seats = 20
APN_beds = 15

total = (PNA_seats + APN_seats)*25 + (PNA_beds + APN_beds)*50
GST = round((total - (total/1.15)), 2)

print(f"Booking: {PNA_seats}, {PNA_beds}, {APN_seats}, {APN_beds}")
print(f"Total: ${total}, GST: ${GST}")