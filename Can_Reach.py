for _ in range(int(input())):
    x, y, k = map(int, input().split())
    if x % k == 0 and y % k == 0:
        ans = "YES"
    else:
        ans = "NO"
    print(ans)