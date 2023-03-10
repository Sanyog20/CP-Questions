for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a = a[::-1]
    ans = 0
    for i in range(n):
        if a[i] < x:
            ans = n - i
            break
    print(ans)