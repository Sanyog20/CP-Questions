for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = []
    if k == 1:
        for i in range(n , 0, -1):
            ans.append(i)
    else:
        a.sort()
        t1 = 0
        t2 = a[0]
        for i in range(k - 1):
            while(t2 > t1):
                ans.append(t2)
                t2 = t2 - 1
            # print(*ans, t2, t1, i)
            t1 = a[i]
            t2 = a[i + 1]
        while(t2 > t1):
            ans.append(t2)
            t2 = t2 - 1
    print(*ans)
