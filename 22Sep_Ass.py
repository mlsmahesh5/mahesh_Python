# If two values are same print error, else print the highest value

a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
c = int(input("Enter third value: "))
d = int(input("Enter fourth value: "))


if a==b or a==c or a==d or b==c or b==d or c==d:
    print("Error")

elif a>b and a>c and a>d:
    print("First value is greater", a)
elif b>c and b>d:
    print("Second value is greater", b)
elif c>d:
    print("Third value is greater", c)
else:
    print("Fourth value is greater", d)

