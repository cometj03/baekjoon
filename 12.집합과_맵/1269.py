# 대칭 차집합
n, m = map(int, input().split())
A = {*map(int, input().split())}
B = {*map(int, input().split())}
intersec_len = len(A & B)

print(n + m - intersec_len*2)