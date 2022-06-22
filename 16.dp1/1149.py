# RGB 거리
import sys
input = sys.stdin.readline

n = N = int(input())
cost = 0
before = -1
while n:
    n -= 1
    r, g, b = map(int, input().split())
    