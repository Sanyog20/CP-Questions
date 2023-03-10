for _ in range(int(input())):
    n = int(input())
    s = input()
    if n % 2 != 0:
        print("NO")
    else:
        t = list(s)
        t.sort()
        c = max(t, key=t.count)
        max_count = s.count(c)
        if max_count > (n / 2):
            print("NO")
        else:
            print("YES")
            t1 = []
            t2 = []
            for i in range(n):
                if i % 2 == 0:
                    t1.append(t[i])
                else:
                    t2.append(t[i])
            t1 = t1 + t2
            s1 = ""
            for i in t1:
                s1 = s1 + i
            print(s1)