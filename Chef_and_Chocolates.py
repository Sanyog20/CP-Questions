for _ in range(int(input())):
    n = int(input())
    t = []
    for i in range(n):
        s = input()
        t.append(s)
    a = max(t, key=t.count)
    if t.count(a) > (n / 2):
        print(a)