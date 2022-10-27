veg = "tomato,50,onion,20,potato,50"
ve = (veg.split(","))
con = ve[1::2]
val = [eval(i) for i in con]
num = 0
for i in val:
    num = num + i
    avg = num / len(val)
print("The average of veg in the market:", avg)
