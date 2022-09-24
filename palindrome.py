# Read the value from the user & checks whether the value is Palindrome or not ?

a = int(input("Enter the number: "))
b = a
num = 0

while a > 0:
    num = (num*10)+(a%10)
    a = a//10
if b == num:
    print(num, "is a Palindrome")
else:
    print(num, "is not a Palindrome")