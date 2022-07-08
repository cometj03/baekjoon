# 오큰수
n = int(input())
arr = [*map(int, input().split())]
stack = [0] # 인덱스를 넣어주는 스택
ans = [-1] * n

for i in range(1, n):
    while stack and arr[i] > arr[stack[-1]]:
        ans[stack.pop()] = arr[i]
    stack.append(i)

print(*ans)