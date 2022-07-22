# 구간 합 구하기 4
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0] + [*map(int, input().split())]

for i in range(2, len(arr)):
    arr[i] += arr[i-1]

while M:
    M -= 1
    a, b = map(int, input().split())
    print(arr[b] - arr[a-1])