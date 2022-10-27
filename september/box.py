# Print box shape


n = 5
r = 1
while r <= n:
    c = 1
    while c <= n:
        if (r == 1) or (r == n) or (c == 1) or (c == n):
            print("*", end="  ")
        else:
            print(" ", end="  ")
        c += 1
    print()
    r += 1
