# Take a No. from the user which is <=1000 and =>10000.
# Find the reverse of a No. in the way that the No. hundred place should be in the unit place.

n = int(input("Enter the number between 1000 to 10000: "))
rev = 0

while n > 100:
    a = n % 10
    rev = rev * 10 + a
    n = n // 10
rev = rev*100 + n

print(rev)
