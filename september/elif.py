# Using elif
a = int(input("enter first value: "))
b = int(input("enter second value: "))
c = int(input("enter third value: "))

if a>b and a>c:
    print("first value greatest")
elif b>a and b>c:
    print("second value is greatest")
elif c>a and c>b:
    print("third value is greatest")

