import math
for _ in range(int(input())):
    x, y = map(int, input().split())
    z = math.ceil((x + y) / 2)
    print(max(abs(z - x), abs(z - y)))