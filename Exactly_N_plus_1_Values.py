for i in range(int(input())):
    n = int(input())
    l = [1]
    for j in range(1, n):
        l .append(j);
    l.append((2 ** n) - sum(l))
    print(*l)