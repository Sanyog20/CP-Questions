for i in range(int(input())):
    x, y = map(int, input().split())
    s = input()
    streak = 0
    max_streak = 0
    for j in range(len(s)):
        if s[j] == '0':
            if streak > max_streak:
                max_streak = streak
            streak = 0
        else:
            streak += 1;
        if streak > max_streak:
            max_streak = streak
    t = s.count('1')
    pay = (x * t) + (y * max_streak)
    print(pay)