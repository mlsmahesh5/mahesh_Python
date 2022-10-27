

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
a = 0
b = 1

if end < 1:
    print(a)

elif start >= 0:
    for i in range(start, end):
        c = a + b
        a = b
        b = c
        if c >= start and c < end:
            print(c)
