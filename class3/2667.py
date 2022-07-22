# 단지번호붙이기
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N = int(input())
mapp = [list(map(int, input())) for _ in range(N)]
houses = []

def bfs(x, y, index):
    q = [(x, y)]
    mapp[y][x] = 0
    houses[index] += 1
    while q:
        a, b = q.pop(0)
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if 0 <= nx < N and 0 <= ny < N and mapp[ny][nx] == 1:
                mapp[ny][nx] = 0
                q.append((nx, ny))
                houses[index] += 1

for i in range(N):
    for j in range(N):
        if mapp[i][j] == 1:
            houses.append(0)
            bfs(j, i, len(houses) - 1)

print(len(houses))
for i in sorted(houses):
    print(i)