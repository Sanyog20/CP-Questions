for i in range(int(input())):
    n, v = map(int, input().split())
    if v == 1:
        min_cost = int(n * (n - 1) / 2)
    elif v >= n - 1:
        min_cost = n - 1
    else:
        t = int((n - v - 1) * (n - v) / 2)
        min_cost = v + t + 1
    max_cost = int(n * ( n - 1) / 2)
    print(max_cost, min_cost)
