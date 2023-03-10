for i in range(int(input())):
    a = list(map(int, input().split()))
    count_0 = 0
    count_1 = 0
    count_2 = 0
    for j in a:
        if j == 0:
            count_0 += 1
        elif j == 1:
            count_1 += 1
        elif j == 2:
            count_2 += 1
    if count_2 == count_1:
        print("DRAW")
    elif count_1 > count_2:
        print("INDIA")
    else:
        print("ENGLAND")