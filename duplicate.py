a = list(map(int, input().split()))
if len(set(a)) == len(a):
    print(-1)
else:
    a.sort()
    ans = []
    for i in range(len(a) - 1):
        if a[i] == a[i + 1] and a[i] not in ans:
            ans.append(a[i])
    print(*ans)
