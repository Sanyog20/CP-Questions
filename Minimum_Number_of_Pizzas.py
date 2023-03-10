import math
for _ in range(int(input())):
    n, k = map(int, input().split())
    t = math.gcd(n, k)
    t = int((n * k) / t)
    print(int(t / k))
