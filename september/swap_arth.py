# swapping 2 variables using arithmetic operators:
a = 20
b = 30
print("a = ", a)
print("b = ", b)
print("Before swap 'a' value is", a, end=" and ")
print("'b' value is", b)

a = a + b
b = a - b
a = a - b
print("a = ", a)
print("b = ", b)
print("After swap 'a' value is", a, end=" and ")
print("'b' value is", b)
