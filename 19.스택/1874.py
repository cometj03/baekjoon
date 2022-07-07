# 스택 수열
n = int(input())
arr = [int(input()) for _ in range(n)]
stack = []
log = []

def test():
    num = 1
    for i in range(n):
        if len(stack) > 0 and stack[-1] > arr[i]:
            return False
        if len(stack) == 0 or stack[-1] < arr[i]:
            while num <= arr[i]:
                stack.append(num)
                log.append("+")
                num += 1
        if stack[-1] == arr[i]:
            stack.pop()
            log.append("-")
    return True

if test():
    print(*log, sep="\n")
else:
    print("NO")