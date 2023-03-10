for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    v = input()
    min_test_case = []
    for i in range(n):
        if v[i] == '0':
            min_test_case.append(s[i])
    print(min(min_test_case))