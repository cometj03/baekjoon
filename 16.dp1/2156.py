# 포도주 시식
n = int(input())
wine = [int(input()) for _ in range(n)] + [0, 0]
drink = [0] * (n+2)

drink[0], drink[1] = wine[0], wine[0] + wine[1]
drink[2] = max(wine[0] + wine[2], wine[1] + wine[2], drink[1])
# 틀린 이유: drink[1]을 고려 대상에서 빠뜨림

for i in range(3, n):
    # 마시지 않는 경우도 고려
    drink[i] = max(wine[i] + drink[i-2], wine[i] + drink[i-3] + wine[i-1], drink[i-1])

print(drink[n-1])