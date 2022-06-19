# 파도반 수열
dp = [0, 1, 1, 1, 2, 2, 3] + [0]*100
m = 7

def p(n):
    if dp[n] != 0:
        return dp[n]
    global m
    for i in range(m, n+1):
        dp[i] = dp[i-1] + dp[i-5]
    m = n
    return dp[n]

T = int(input())
while T:
    T -= 1
    N = int(input())
    print(p(N))