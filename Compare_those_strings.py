for _ in range(int(input())):
    n = int(input())
    s1 = input()
    s2 = input()
    count = 0
    max_count = 0
    for i in range(n):
        if s1[i] <= s2[i] and i != n - 1:
            count += 1
        elif s1[i] < s2[i] and i == n - 1:
            count += 1
        elif s1[i] > s2[i]:
            if count > max_count:
                max_count = count
            count = 0
    print(max(max_count, count))