# Calculation of Electric Bill if less than 90 units No Charge
# From 100 to 150 units Rs: 4 per unit, From 150 units Rs: 10 per unit

units = int(input("Enter number of Units consumed: "))

if units < 100:
    print("No charge")
elif units > 100 and units < 150:
    fifty_units = (units-100)*4
    print(fifty_units)
elif units > 150:
    a = units-100
    b = a-50
    bill = (b*10) + (50*4)
    print(bill)