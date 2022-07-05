# 쉬운 계단 수
n = int(input())
dp = [[0]*10, [0] + [1]*9] + [[0]*10 for _ in range(100)] # 마지막 자리 숫자의 개수

for i in range(2, n+1):
    # 양 끝 점
    dp[i][0] += dp[i-1][1]
    dp[i][9] += dp[i-1][8]
    # 나머지 숫자들
    for j in range(1, 9):
        dp[i][j] += dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n]) % 1_000_000_000)