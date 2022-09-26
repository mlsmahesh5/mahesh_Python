# print first letter of your name

n = 5
r = 1
while r <= n:
    c = 1
    while c <= n:
        if (c == 1) or (r == 2 and c != 3) or (r == 3 and c ==3 ) or (c == 5):
            print("*", end="  ")
        else:
            print(" ", end="  ")
        c += 1
    print()
    r += 1