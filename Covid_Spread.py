for _ in range(int(input())):
    n, d = map(int, input().split())
    infected = 1
    i = 0
    while(infected < n and i < d):
        if i < 10:
            infected = infected * 2
        else:
            infected = infected * 3
        i = i + 1
    print(min(infected, n))
