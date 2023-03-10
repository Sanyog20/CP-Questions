for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = []
    arr.sort()
    for j in range(n - 1):
        if arr[j] == arr[j + 1]:
            ans.append(arr[j])
    if arr[n - 2] == arr[n - 1]:
        ans.append(arr[n - 1])
    ans.append(arr[n - 1])
    arr = arr[::-1]
    for j in range(1, n - 1):
        if arr[j] != arr[j + 1]:
            ans.append(arr[j])
    if arr[n - 2] != arr[n - 1]:
        ans.append(arr[n - 1]) 
    for j in range(len(ans) - 1):
        if ans[j] == ans[j + 1]:
            ans = [-1]
            break
    print(*ans)