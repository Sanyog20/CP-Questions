for _ in range(int(input())):
    n = int(input())
    s = input()
    time = 0
    i = 0
    flag = 0
    while i < n - 1:
        if s[i] == s[i + 1]:
            time = time + 1
            i = i + 2
            flag = 2
        else:
            time = time + 1
            i = i + 1
            flag = 1
    if i == n - 1 and flag == 2:
        time += 1
    if flag == 1:
        if s[n - 1] != s[n - 2]:
            time += 1
    print(time)