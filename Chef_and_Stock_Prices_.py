for _ in range(int(input())):
    s, a, b, c = map(int, input().split())
    t = s + ((s * c) / 100)
    if t >= a and t <= b:
        print("Yes")
    else:
        print("No")