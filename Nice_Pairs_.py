for i in range(int(input())):
    n = int(input())
    s = input()
    count = 0
    for j in range(n - 1):
        for k in range(j + 1, n):
            if abs(int(s[j]) - int(s[k])) == k - j:
                count += 1
    print(count)