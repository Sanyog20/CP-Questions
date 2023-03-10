for i in range(int(input())):
    n = int(input())
    s = input()
    ans = "YES"
    if n < 2:
        ans = "NO"
    else:
        ans = "NO"
        for j in range(n - 1):
            if s[j] == s[j + 1]:
                ans = "YES"
    print(ans)