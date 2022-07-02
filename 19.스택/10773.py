# 제로
stack = []
n = int(input())
while n:
    n -= 1
    a = int(input())
    if a == 0:
        stack.pop()
        continue
    stack.append(a)
print(sum(stack))