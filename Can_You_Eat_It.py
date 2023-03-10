for _ in range(int(input())):
    n, k = map(int, input().split())
    if n % k == 0:
        ans = n // k
    else:
        ans = -1
    print(ans)