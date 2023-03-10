for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a = a[::-1]
    count = 0
    coins = 0
    for i in a:
        coins = coins + i
        count += 1
        if coins >= x:
            break
    if coins >= x:
        print(count)
    else:
        print(-1)