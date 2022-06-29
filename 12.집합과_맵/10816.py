# 숫자 카드2
tenbillion = 10_000_000
memo = [0] * (tenbillion*2 + 1)
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
check_list = list(map(int, input().split()))

for i in arr:
    memo[i+tenbillion] += 1

for i in check_list:
    print(memo[i+tenbillion], end=" ")