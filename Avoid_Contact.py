for _ in range(int(input())):
    x, y = map(int, input().split())
    if y == 0:
        print(x)
    elif x == y:
        print(x + y - 1)
    else:
        print((y * 2) + (x - y))