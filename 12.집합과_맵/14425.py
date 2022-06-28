# 문자열 집합
n, m = map(int, input().split())
arr = {input() for _ in range(n)}
check = [input() for _ in range(m)]
cnt = 0

for c in check:
    if c in arr:
        cnt += 1
print(cnt)