# Function to get sum of digits

def getSum(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum


n = 269
print(getSum(n))
