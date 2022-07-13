# 요세푸스 문제 0
N, K = map(int, input().split())
q = [i for i in range(1, N+1)]
ans = []

# 앞에 거 뒤로 n번 옮김
def change(n):
    for _ in range(n):
        q.append(q.pop(0))

while N:
    N -= 1
    change(K-1)
    ans.append(q.pop(0))

print("<", end="")
print(*ans, sep=", ", end="")
print(">")