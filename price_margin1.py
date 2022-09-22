original_price = int(input("Enter Tomato price : "))

if original_price >= 50:
    original_price = original_price + (original_price * 20 / 100)
    print("Final price of tomato is:", original_price)

if original_price <= 49:
    original_price = original_price + (original_price * 40 / 100)
    print("Final price of tomato is:", original_price)
