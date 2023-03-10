for _ in range(int(input())):
    n, k, x = map(int, input().split())
    if x > k:
        print(-1)
    elif x == k:
        t = []
        for i in range(x):
            t.append(i)
        t1 = t
        for i in range(n // k):
            t1 = t1 + t
        print(*(t1[:n]))
    else:
        t = []
        for i in range(x):
            t.append(i)
        t.append(x + 1)
        t1 = t
        for i in range(n // x):
            t1 = t1 + t
        print(*(t1[:n]))
