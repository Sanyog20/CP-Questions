import math
for _ in range(int(input())):
    n = int(input())
    t = 0
    t1 = math.factorial(n)
    for i in range(1, n + 1):
        t = t + (i * t1 * (n - 1))
    print(int(t / math.factorial(n)))