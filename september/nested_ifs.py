# Using nested ifs

card_valid = input("insert the card? ")
if card_valid == "yes":
    pin = int(input("enter your pin: "))
    if pin == 1234:
        amount = int(input("enter amount: "))
        if amount <= 1500 and amount%100 == 0:
            print("You have withdrawn amount")
        else:
            print("invalid")
    else:
        print("invalid pin")
else:
    print("invalid card")
