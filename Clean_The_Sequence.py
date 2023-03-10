for _ in range(int(input())):
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0
    for i in range(k - 1):
        if a[i] != a[i + 1]:
            count += 1
    t = n
    h = []
    while(t):
        if count == 0:
            h.append(count)
        else:
            h.append(count - 1)
        t -= 1
    for i in range(k - 1):
        if a[i] != a[i + 1]:
            if i != 0 and i != (k - 1):
                h[a[i] - 1] -= 1
                h[a[i + 1] - 1] -= 1
            elif i == 0:
                h[a[i + 1] - 1] -= 1
            else:
                h[a[i] - 1] -= 1
    print(*h)
