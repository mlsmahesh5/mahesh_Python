# Print even numbers from the range values entered by the user

start_value = int(input("Enter Start range value: "))
end_value = int(input("Enter Start range value: "))

for x in range(start_value, end_value ):
    if x%2 == 0:
        print(x, end=" ")