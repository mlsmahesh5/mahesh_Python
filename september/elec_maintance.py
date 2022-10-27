# maintenance charge 100 for units <150 and charge 500 for units > 150

units = int(input("Enter number of units: "))

if units <= 100:
    print("Your bill is", 0 + 100)
elif units <= 150:
    print("Your bil is", (units-100)*4 + 100)
else:
    print("Your bill is", (50*4)+(units-150)*10 + 500)
