for _ in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))
    a = []
    a.append(b[0])
    for i in range(1, len(b)):
        if b[i] == b[i - 1]:
            a.append(b[i])
        elif b[i] < b[i - 1] and b[i] != 1:
            a.append(b[i])
        elif b[i] > b[i - 1]:
            a = [-1]
            break
    print(*a)
