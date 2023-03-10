for _ in range(int(input())):
    n, m = map(int, input().split())
    if n % m == 0 and (n // m % 2) == 0:
        print("Yes")
    else:
        print("No")
