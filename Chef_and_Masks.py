for _ in range(int(input())):
    x, y = map(int, input().split())
    t = y / 10
    if x < t:
        print("Disposable")
    else:
        print("Cloth")
