for i in range(int(input())):
    n, x, p = map(int, input().split())
    marks = (x * 3) - (n - x)
    if marks >= p:
        print("PASS")
    else:
        print("FAIL")