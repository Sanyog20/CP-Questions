for _ in range(int(input())):
    x, y, z = map(int, input().split())
    profit = (z - y) * x
    print(profit)