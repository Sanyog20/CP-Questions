for _ in range(int(input())):
    s = input()
    t = input()
    for i in range(5):
        if s[i] == t[i]:
            print("G", end="")
        else:
            print("B", end="")
    print()
