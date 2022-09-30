# Sum of odd numbers from 150 to 300

total = 0
for i in range (150, 300):
    if i%2 != 0:
     total = total + i
print(total)