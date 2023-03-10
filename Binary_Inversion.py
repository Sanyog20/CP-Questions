for _ in range(int(input())):
    n, m = map(int, input().split())
    s = []
    for i in range(n):
        s1 = input()
        s.append(s1)
    s.sort()
    t = ""
    ans = 0
    for i in s:
        t = t + i
    t = list(t)
    t1 = t.count('1')
    one_count = 0
    l = len(t)
    for i in range(l):
        if t[i] == '1':
            t2 = l - i - one_count - 1
            ans = ans + t2
            one_count += 1
    print(ans)
