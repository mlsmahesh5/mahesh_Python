# Using if elif and else:
a = int(input("enter first value: "))
b = int(input("enter second value: "))
c = int(input("enter third value: "))

if a>b and a>c:
    print("first value greatest")
elif b>c:
    print("second value is greatest")
else:
    print("third value is greatest")
