# print n fibonacci numbers

n = int(input("Enter number: "))
a = 0
b = 1

if n < 1:
    print(a)
for i in range(n):
    c = a + b
    a = b
    b = c
    print(c, end=" ")
