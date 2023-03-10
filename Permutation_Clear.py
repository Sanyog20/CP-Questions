for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())
    b = list(map(int, input().split()))
    for i in b:
        a.remove(i)
    print(*a)