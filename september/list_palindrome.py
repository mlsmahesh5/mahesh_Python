input_string = input("Enter elements of a list separated by space: ")
print("\n")
user_list = input_string.split()
print("list: ", user_list)
c = 0

# convert each item to int type
for i in range(len(user_list)):
    # convert each item to int type
    user_list[i] = int(user_list[i])

# loop till list is not empty
for i in user_list:
    # Find reverse of current number
    t = i
    rev = 0
    while t > 0:
        rev = rev * 10 + t % 10
        t = t // 10
    # compare rev with the current number
    if rev == i:
        print("Palindrome numbers in the list:", i)
        c = c + i

