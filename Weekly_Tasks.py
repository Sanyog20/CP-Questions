for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    t = n % sum(a)
    if t == 0:
        print(7)
    else:
        ans = 0
        for i in a:
            ans += 1
            t = t - i
            if t <= 0:
                break
        print(ans)
