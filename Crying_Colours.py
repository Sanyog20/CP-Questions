for _ in range(int(input())):
    n = int(input())
    r1, g1, b1 = map(int, input().split())
    r2, g2, b2 = map(int, input().split())
    r3, g3, b3 = map(int, input().split())
    operations = r3 + r2
    if r2 > g1:
        b2 = b2 + (r2 - g1)
    elif r3 > b1:
        g3 = g3 + (r3 - b1)
    operations = operations + b2
    print(operations)
