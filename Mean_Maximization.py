for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    s = sum(a) - a[-1]
    t = (s / (n - 1)) + a[-1]
    print(t)