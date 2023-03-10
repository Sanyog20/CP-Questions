for _ in range(int(input())):
    n = int(input())
    a = [3]
    n = n - 1
    t = 2
    while n:
        a.append(a[-1] + t)
        t = t * 2
        n = n - 1
    print(*a)