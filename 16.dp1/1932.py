# 정수 삼각형
n = int(input())
arr = []

for _ in range(n):
    nums = list(map(int, input().split()))
    arr.append(nums)

for i in range(1, n):
    arr[i][0] += arr[i-1][0]
    arr[i][-1] += arr[i-1][-1]
    for j in range(1, i):
        arr[i][j] += max(arr[i-1][j], arr[i-1][j-1])

print(max(arr[n-1]))
