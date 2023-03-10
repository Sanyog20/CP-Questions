for _ in range(int(input())):
    n, k = map(int, input().split())
    s = list(input())
    for i in range(n - k + 1):
        if s[i] == '1':
            for j in range(i, i + k):
                if s[j] == '0':
                    s[j] = '1'
                else:
                    s[j] = '0'
    for i in range(n):
        print(s[i], end="")
    print()