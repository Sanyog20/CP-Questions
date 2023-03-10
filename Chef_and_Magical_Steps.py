def isPrime(x):
    prime_flag = 0
    if x == 2:
        return True
    elif x % 2 == 0:
        return False
    for j in range(3, int(x ** 0.5) + 1, 2):
        if (x % j == 0):
            prime_flag = 1
            break
    if prime_flag == 0:
        return True
    else:
        return False


def Prime(x, y):
    count = 0
    for i in range(x + 1, y + 1):
        if isPrime(i):
            count += 1
    return count
        


for i in range(int(input())):
    x, y = map(int, input().split())
    steps = y - x - Prime(x, y)
    if x == 2:
        steps += 2
    if isPrime(x + 1):
        steps -= 1
    print(steps)
