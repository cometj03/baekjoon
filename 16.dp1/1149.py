# RGB 거리
# Desc: i번째 집을 각각의 색으로 칠할 때, 1~i번째 집을 모두 칠하는 최소 비용으로 부분문제를 정의해봅시다.
import sys
input = sys.stdin.readline

n = int(input())
rgb = []
before = -1

for i in range(n):
    r, g, b = map(int, input().split())
    rgb.append([r, g, b])
    
for i in range(1, n):
    # red
    rgb[i][0] = min(rgb[i-1][1], rgb[i-1][2]) + rgb[i][0]
    # green
    rgb[i][1] = min(rgb[i-1][0], rgb[i-1][2]) + rgb[i][1]
    # red
    rgb[i][2] = min(rgb[i-1][0], rgb[i-1][1]) + rgb[i][2]

print(min(rgb[n-1]))