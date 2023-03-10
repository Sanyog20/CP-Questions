t = []
b = []

def isPrime(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        if n % 2 == 0:
            return 0
        else:
            for i in range(3, int(n ** 0.5) + 1, 2):
                if n % i == 0:
                    return 0
            return 1

for i in range(1, 10000):
    if isPrime(i):
        t.append(i)

count = 0
for i in range(1, 100000):
    if i in t:
        b.append(count)
    else:
        count = count + 1
        b.append(count)

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = 1
    for i in range(n):
        if (i + 1) in t:
            s = s * b[a[i] - 1]
        else:
            s = s * (a[i] - b[a[i] - 1])
    print(s)
