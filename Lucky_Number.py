for i in range(int(input())):
    a, b, c = map(int, input().split())
    if a == 7 or b == 7 or c == 7:
        print("YES")
    else:
        print("NO")
