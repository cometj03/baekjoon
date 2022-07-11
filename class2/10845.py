# 큐
import sys
input = sys.stdin.readline

N = int(input())
q = []

while N:
    N -= 1
    tmp = input().split()

    if "push" in tmp:
        num = int(tmp[1])
        q.append(num)
    elif "pop" in tmp:
        if len(q) == 0:
            print(-1)
            continue
        print(q.pop(0))
    elif "size" in tmp:
        print(len(q))
    elif "empty" in tmp:
        print(int(len(q) == 0))
    elif "front" in tmp:
        if len(q) == 0:
            print(-1)
            continue
        print(q[0])
    elif "back" in tmp:
        if len(q) == 0:
            print(-1)
            continue
        print(q[-1])

