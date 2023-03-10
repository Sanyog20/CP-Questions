for _ in range(int(input())):
    n, k = map(int, input().split())
    ans = []
    for i in range(1, n + 1):
        ans.append(i)
    if (n - k) % 2 == 0:
        for i in range(k, n - 1, 2):
            ans[i], ans[i + 1] = ans[i + 1], ans[i]
    else:
        for i in range(k, n - 1, 2):
            ans[i], ans[i + 1] = ans[i + 1], ans[i]
        ans[0], ans[-1] = ans[-1], ans[0]
    print(*ans)