# 구간 합 구하기

# TODO: 시간초과
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

while M:
    M -= 1
    i, j = map(int, input().split())
    print(sum(arr[i-1:j]))