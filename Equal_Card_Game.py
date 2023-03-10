for _ in range(int(input())):
    k = int(input())
    if k % 52 == 0:
        print(0)
    else:
        t = int(52 / k)
        print(52 - (t * k))