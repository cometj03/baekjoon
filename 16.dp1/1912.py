# 연속합
n = int(input())
arr = list(map(int, input().split()))
dp = [arr[0]] # i 번째에는 i 번째 데이터와 이전 데이터를 포함한 데이터의 합 중 최대값이 들어감

for i in range(1, n):
    # dp[i-1]에 이미 최대값이 들어가 있으므로 아래 두 요소만 비교하면 됨.
    M = max(dp[i-1] + arr[i], arr[i]) 
    dp.append(M)
print(max(dp))