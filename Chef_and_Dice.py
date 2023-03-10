a, b = map(int, input().split())
if (a + b) % 2 != 0:
    print("Garden")
else:
    if a == b:
        print("Coding")
    else:
        print("Chess")