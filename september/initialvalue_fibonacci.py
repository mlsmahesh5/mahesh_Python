# 10 fibonacci numbers based on 2 initial values

first = int(input("enter first value: "))
second = int(input("enter second value: "))

for i in range(0,10):
    result = first + second
    first = second
    second = result
    print(result, end=" ")

