for _ in range(int(input())):
    d1, d2, d3 = map(int, input().split())
    s1, s2, s3 = map(int, input().split())
    d4 = d1 + d2 + d3
    s4 = s1 + s2 + s3
    if d4 > s4:
        print("DRAGON")
    elif s4 > d4:
        print("SLOTH")
    else:
        if d1 > s1:
            print("DRAGON")
        elif s1 > d1:
            print("SLOTH")
        else:
            if d2 > s2:
                print("DRAGON")
            elif s2 > d2:
                print("SLOTH")
            else:
                print("TIE")