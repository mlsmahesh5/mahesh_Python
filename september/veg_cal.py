# Calculation of vegetables details in the market:

veg = ["tomato", 60.5, 100, "cucumber", 50, 190, "potato", 60, 500]

price = (veg[1::3])
avg_price = sum(price)//3

weight = (veg[2::3])
ton_weight = sum(weight)/1000

print("Prices of vegetables", price)
print("Average price of vegetables in the market:", avg_price, "\n")

print("Quantity of vegetables", weight)
print("Total quantity of vegetables in the market in Tons:", ton_weight)
