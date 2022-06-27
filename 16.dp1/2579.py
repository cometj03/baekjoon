# 계단 오르기
n = int(input())
scores = [int(input()) for _ in range(n)] + [0, 0] # n이 3미만일 때 대비
dp = [0] * (n+3)

dp[0] = scores[0]
dp[1] = scores[0] + scores[1]
dp[2] = max(scores[0], scores[1]) + scores[2]
for i in range(3, n):
    dp[i] = max(dp[i-3] + scores[i-1], dp[i-2]) + scores[i]

print(dp[n-1])