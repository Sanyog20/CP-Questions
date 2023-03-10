for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    s1 = bin(s).replace("0b", "")
    if s1.count('1') == 1:
        print(0)
    else:
        t = (2 ** len(s1)) - s
        t1 = min(a)
        l1 = a.index(t1)
        a1 = int(1 + (t / t1))
        print(1)
        print(1, a1)
        print(l1 + 1)