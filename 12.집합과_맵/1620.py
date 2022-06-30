# 나는야 포켓몬 마스터 이다솜
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
book = {}
memo = [""] * (n+1)

for i in range(1, n+1):
    name = input()[:-1]
    book[name] = i
    memo[i] = name

for _ in range(m):
    test = input()[:-1]
    if test.isnumeric():
        num = int(test)
        print(memo[num])
    else:
        print(book[test])