# Print X inside a box in * shape


n = 5
r = 1
while r <= n:
    c = 1
    while c <= n:
        if (r == 1) or (r == n) or (c == 1) or (c == n) or (r == c) or (r+c == n+1):
            print("*", end="  ")
        else:
            print(" ", end="  ")
        c += 1
    print()
    r += 1
