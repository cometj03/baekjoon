# 1로 만들기
n = int(input())
memo = [0, 0, 1, 1] + [0]*n

for i in range(4, n+1):
    case = [memo[i-1]]
    if n % 3 == 0:
        case.append(memo[i//3])
    if n % 2 == 0:
        case.append(memo[i//2])
    memo[i] = min(case) + 1

print(memo[n])