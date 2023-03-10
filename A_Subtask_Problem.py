for i in range(int(input())):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    if 0 not in a:
        points = 100
    else:
        t = a.index(0)
        if t >= m:
            points = k
        else:
            points = 0
    print(points)