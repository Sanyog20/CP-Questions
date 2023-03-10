for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = "YES"
    for i in range(max(a) + 1):
        if i not in a:
            break
        elif a.count(i) < 2:
            ans = "NO"
            break
    print(ans)