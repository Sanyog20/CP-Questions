counter = 1
a = []
for i in range(500):
    a.append(2 * counter)
    a.append((2 * counter) - 1)
    counter = counter + 1

for _ in range(int(input())):
    n = int(input())
    print(*a[:n])