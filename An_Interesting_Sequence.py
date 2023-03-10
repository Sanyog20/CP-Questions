for _ in range(int(input())):
    k = int(input())
    count = 0
    while(k % 2 == 0):
        count = count + 1
        k = k / 2
    print(count)
