for _ in range(int(input())):
    n, a = map(int, input().split())
    healthy = n - a
    print(min(a, healthy))
    