# 주유소
N = int(input())
road = [*map(int, input().split())]
price = [*map(int, input().split())]
cost = 0

i = 0
while i < N - 1:
    length = road[i]
    k = i + 1
    while k < N-1 and price[k] >= price[i]:
        length += road[k]
        k += 1
    cost += length * price[i]
    i = k

print(cost)