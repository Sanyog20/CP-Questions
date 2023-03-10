for _ in range(int(input())):
    mean, median = map(int, input().split())
    p = mean - 1
    q = mean
    r = mean + 1
    if q == median:
        print(p, q, r)
    else:
        t = median - q
        if t > 0:
            p = p - (2 * t)
            q = median
            r = median + 1
            print(min(p, r), q, max(p, r))
        else:
            r = r - (2 * t)
            q = median
            p = median - 1
            print(min(p, r), q, max(p, r))
