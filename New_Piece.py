for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    if a == c and b == d:
        print(0)
    elif (a + b) % 2 == 0 and (c + d) % 2 == 0:
        print(2)
    elif (a + b) % 2 == 1 and (c + d) % 2 == 1:
        print(2)
    else:
        print(1)