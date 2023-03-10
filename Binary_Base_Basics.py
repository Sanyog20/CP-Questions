for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    i = 0
    j = n - 1
    count = 0
    while(i <= j):
        if s[i] != s[j]:
            count = count + 1
        i = i + 1
        j = j - 1
    if k == count:
        print("YES")
    elif((k - count) % 2 == 0) and k > count:
        print("YES")
    else:
        print("NO")
