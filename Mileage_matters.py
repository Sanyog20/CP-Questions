for _ in range(int(input())):
    n, x, y, a, b = map(int, input().split())
    if (x / a) < (y / b):
        print("PETROL")
    elif (x / a) > (y / b):
        print("DIESEL")
    else:
        print("ANY")