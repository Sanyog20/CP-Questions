def most_frequent(List):
    dict = {}
    count, itm = 0, ''
    for item in reversed(List):
        dict[item] = dict.get(item, 0) + 1
        if dict[item] >= count :
            count, itm = dict[item], item
    return(itm)

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    t = most_frequent(a)
    t = a.count(t)
    if n % 2 == 0:
        if t > (n / 2):
            print("No")
        else:
            print("Yes")
    else:
        if t > int(n / 2) + 1:
            print("No")
        else:
            print("Yes")
 