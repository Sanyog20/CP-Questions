for _ in range(int(input())):
    n = int(input())
    A = []
    for i in range(n, 0, -1):
        A.append(i)
    print(*A)
