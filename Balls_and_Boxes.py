for _ in range(int(input())):
    n, k = map(int, input().split())
    t = (k * (k + 1)) / 2
    if t <= n:
        print("YES")
    else:
        print("NO")