for _ in range(int(input())):
    n = int(input())
    s = bin(n).replace("0b", "")
    t = len(s)
    n1 = n + pow(2, t)
    n2 = n + pow(2, t + 1)
    print(n, n1, n2)