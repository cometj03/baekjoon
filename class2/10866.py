# 덱
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
q = deque()
size = 0

while N:
    N -= 1
    tmp = input().split()
    if tmp[0] == "push_front":
        num = int(tmp[1])
        q.appendleft(num)
        size += 1
    elif tmp[0] == "push_back":
        num = int(tmp[1])
        q.append(num)
        size += 1
    elif tmp[0] == "pop_front":
        if size == 0:
            print(-1)
            continue
        print(q.popleft())
        size -= 1
    elif tmp[0] == "pop_back":
        if size == 0:
            print(-1)
            continue
        print(q.pop())
        size -= 1
    elif tmp[0] == "size":
        print(size)
    elif tmp[0] == "empty":
        print(int(size == 0))
    elif tmp[0] == "front":
        if size == 0:
            print(-1)
            continue
        print(q[0])
    elif tmp[0] == "back":
        if size == 0:
            print(-1)
            continue
        print(q[-1])