# 회의실 배정
import sys
input = sys.stdin.readline

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
count = 1

arr.sort(key=lambda x: x[0])
arr.sort(key=lambda x: x[1])

tmp = arr[0]
for i in range(1, n):
    if tmp[1] <= arr[i][0]:
        count += 1
        tmp = arr[i]
print(count)