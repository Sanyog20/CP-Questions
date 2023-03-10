alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'x', 'y', 'z']
for _ in range(int(input())):
    n, q = map(int, input().split())
    a = input()
    b = input()
    for i in range(q):
        l, r = map(int, input().split())
        s1 = list(a[l : r + 1])
        s2 = list(b[l : r + 1])
        