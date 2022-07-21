# 유기농 배추
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while T:
    T -= 1
    M, N, K = map(int, input().split())

    ground = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]

    while K:
        K -= 1
        x, y = map(int, input().split())
        ground[y][x] = 1

    def bfs(x, y):
        visited[y][x] = True
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx] and ground[ny][nx] == 1:
                bfs(nx, ny)

    ans = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and ground[i][j] == 1:
                bfs(j, i)
                ans += 1

    print(ans)