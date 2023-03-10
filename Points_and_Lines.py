for _ in range(int(input())):
    n = int(input())
    x = []
    y = []
    for i in range(n):
        t1, t2 = map(int, input().split())
        x.append(t1)
        y.append(t2)
    x = list(set(x))
    y = list(set(y))
    print(len(x) +  len(y))