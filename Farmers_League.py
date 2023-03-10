for _ in range(int(input())):
    n = int(input())
    matches = int(n * (n - 1) / 2)
    total_score = matches * 3
    max_team = (n - 1) * 3
    remaining_score = total_score - max_team
    if remaining_score % (n - 1) == 0:
        second = remaining_score / (n - 1)
    else:
        second = (remaining_score // (n - 1)) + 2
    print(int(max_team - second))
