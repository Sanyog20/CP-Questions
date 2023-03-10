for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    count = 0
    t = '0' * k
    for i in range(n):
        if s[i] == '1':
            s1 = s[:i]
            s1 = s1 + "0"
            s1 = s1 + s[i + 1:]
            count = max(count, s1.count(t))
    print(count)