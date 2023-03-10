for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    freq = {}
    for item in a:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
    print(freq)
