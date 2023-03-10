for _ in range(int(input())):
    n, k = map(int, input().split())
    ans = n // k
    if n % k != 0:
        ans += 1
    print(ans)