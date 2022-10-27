# Price increasing by margin value
original_price = int(input("Enter Tomato price : "))

greater_than = 20
less_than = 40

if original_price >= 50:
    original_price += (original_price * greater_than / 100)
    print("Final price of tomato is:", original_price)

if original_price <= 49:
    original_price += (original_price * less_than / 100)
    print("Final price of tomato is:", original_price)
