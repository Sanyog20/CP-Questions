for _ in range(int(input())):
    l, a, b = map(int, input().split())
    if l * l == a * b:
        print("Draw")
    elif l * l > a * b:
        print("Chef")
    else:
        print("Divyam")