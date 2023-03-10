def solve(n):
    for j in range(3, n + 1, 2):
        if n % j == 0:
            ans = j
            break
    return ans

for i in range(int(input())):
    n, a, b = map(int, input().split())
    points = 0
    while(n != 1):
        if n % 2 == 0:
            if a > 0:
                if n % 16 == 0:
                    n = int(n / 16)
                    points = points + (4 * a)
                elif n % 8 == 0:
                    n = int(n / 8)
                    points = points + (3 * a)
                elif n % 4 == 0:
                    n = int(n / 4)
                    points = points + (2 * a)
                else:
                    n = int(n / 2)
                    points = points + a
            else:
                n = int(n / n)
                points = points + a
        else:
            if b > 0:
                t = solve(n)
                n = int(n / t)
                points = points + b
            else:
                n = int(n / n)
                points = points + b
    print(points)
