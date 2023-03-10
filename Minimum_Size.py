for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    p = int(input())
    a.sort(reverse=True)
    b.sort(reverse=True)
    k = 0
    flag = 0
    a1 = 0
    b1 = 0
    for i in range(min(n, m)):
        k = k + 1
        a1 = a1 + a[i]
        b1 = b1 + b[i]
        if a1 * b1 >= p:
            flag = 1
            break
    if flag == 1:
        print(k)
    else:
        print(-1)
