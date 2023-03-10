import math
for _ in range(int(input())):
    n, x = map(int, input().split())
    if (x > (3 * n)):
        print("NO")
    elif (x == (3 * n) - 2) or (x == (3 * n) - 1) or (x == (3 * (n - 1)) - 2):
        print("NO")
    else:
        print("YES")
        a = math.ceil(x / 3)
        b = (a * 3) - x
        c = n - (a + b)
        print(a, b, c)
