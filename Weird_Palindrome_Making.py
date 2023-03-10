for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    count_odd = 0
    for j in arr:
        if j % 2 != 0:
            count_odd += 1
        count = int(count_odd / 2)
    print(count)