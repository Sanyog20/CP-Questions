for _ in range(int(input())):
    n = int(input())
    l = ['a', 'b', 'c']
    s = ""
    for i in range(1, n + 1):
        s = s + l[i % 3]
    print(s)