for i in range(int(input())):
    x, y = map(int, input().split())
    if x % 2 == 0 and y % 2 == 0:
        print("YES")
    else:
        if y % 2 != 0 and x % 2 == 0 and x >= 2:
            print("YES")
        else:
            print("NO")