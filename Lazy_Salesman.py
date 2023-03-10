for _ in range(int(input())):
    n, w = map(int, input().split())
    a = list(map(int, input().split()))
    work = 0
    a.sort()
    a = a[::-1]
    money = 0
    for i in range(n):
        money = money + a[i]
        work = work + 1
        if money >= w:
            break
    print(n - work)