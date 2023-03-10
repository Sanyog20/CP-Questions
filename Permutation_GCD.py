for _ in range(int(input())):
    n, x = map(int, input().split())
    if x < n:
        print(-1)
    elif x == n:
        for i in range(1, n + 1):
            print(i, end=" ")
        print()
    else:
        print(x - n + 1, end=" ")
        for i in range(1, n + 1):
            if(i != x - n + 1):
                print(i, end=" ")
        print()