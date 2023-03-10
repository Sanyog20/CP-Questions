for i in range(int(input())):
    x, y, a, b, k = map(int, input().split())
    x = x + (a * k)
    y = y + (b * k)
    if x > y:
        print("DIESEL")
    elif y > x:
        print("PETROL")
    else:
        print("SAME PRICE")