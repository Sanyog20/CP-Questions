for i in range(int(input())):
    x, y = map(int, input().split())
    if y > x:
        if (x % 2 == 0 and y % 2 == 1) or (x % 2 == 1 and y % 2 == 0):
            t = y - x
            ans = int(t / 2) + 2
        else:
            ans = int((y - x) / 2)
    else:
        ans = x - y
    print(ans)