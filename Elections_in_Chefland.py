for _ in range(int(input())):
    a, b, c = map(int, input().split())
    d = max(a, b, c)
    if a > 50:
        print("A")
    elif b > 50:
        print("B")
    elif c > 50:
        print("C")
    else:
        print("NOTA")